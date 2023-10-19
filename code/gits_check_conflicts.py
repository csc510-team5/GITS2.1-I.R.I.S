import subprocess
import json
from parse_diff import normalize_line_endings, get_common_modified_lines
from get_file_at_version import get_file_at_version
from get_github_owner_repo import get_github_owner_repo

def check_conflicts(args):
    target_branch = ""
    merge_base = ""
    target_branches = ["main", "master"]
    for branch in target_branches:
        merge_base = git_merge_base(branch)
        if (len(merge_base) != 0):
            target_branch = branch
            break
    if (len(merge_base) == 0):
        print("Could not locate the merge base!")
        return

    modified_files = git_modified_files(merge_base)
    if (not modified_files):
        print("There are no files modified locally!")
        return

    recent_prs = get_recent_prs(target_branch)
    if (not recent_prs):
        print("Could not fetch recent pull requests!")
        return
    if (len(recent_prs["data"]["repository"]["pullRequests"]["nodes"]) == 0):
        print("There are no pull requests to compare with")
        return
    recent_prs = recent_prs["data"]["repository"]["pullRequests"]["nodes"]
    recent_prs = [
        {**pr, "filePaths": [node["path"] for node in pr["files"]["nodes"]]}
        for pr in recent_prs
    ]

    common_file_prs = [
        {**pr, 'commonFilePaths': list(set(pr.get('filePaths', [])) & set(modified_files))}
        for pr in recent_prs
        if not set(modified_files).isdisjoint(pr.get('filePaths', []))
    ]
    if (not common_file_prs):
        print("There are no conflicting pull requests!")
        return

    file_to_pr = {}
    for pull_request in common_file_prs:
        pr = {
            "filesUrl": f"{pull_request['url']}/files",
            "number": pull_request["number"],
            "title": pull_request["title"],
            "author": dict(pull_request["author"])["login"],
            "baseRef": pull_request["baseRefOid"],
            "headRef": dict(dict(pull_request["headRef"])["target"])["oid"],
            "hasConflict": False,
            "skipped": False
        }

        for path in pull_request.get("commonFilePaths", []):
            if path in file_to_pr:
                file_to_pr[path].append(pr)
            else:
                file_to_pr[path] = [pr]

    for file in file_to_pr:
        for pr in file_to_pr[file]:
            local_base = normalize_line_endings(git_file_at_version(file, merge_base))
            pr_base = normalize_line_endings(get_file_at_version(file, pr["baseRef"]))

            if(local_base != pr_base):
                pr["skipped"] = True
                continue

            local_head = normalize_line_endings(get_local_file(file))
            pr_head = normalize_line_endings(get_file_at_version(file, pr["headRef"]))

            common_modified_lines = get_common_modified_lines(pr_base, local_head, pr_head)
            if (len(common_modified_lines) != 0):
                pr["hasConflict"] = True
                pr["commonModifiedLines"] = common_modified_lines


    conflicts = {
        file: [pr for pr in pr_list if pr["hasConflict"]]
        for file, pr_list in file_to_pr.items()
        if any(pr["hasConflict"] for pr in pr_list)
    }
    if(not conflicts):
        print("There were no merge conflicts detected!")
        return

    result = "\nConflicts were found in the following files: \n"
    for file in conflicts:
        result += f"\n'{file}':\n"
        for pr in conflicts[file]:
            result += f"\tPR #{pr['number']}: {pr['title']}\n"
            result += f"\tAuthor: {pr['author']}\n"
            result += f"\tConflict lines: [{', '.join(map(str, pr['commonModifiedLines']))}]\n"
            result += f"\tPR changes: {pr['filesUrl']}\n"

    print(result)

def git_merge_base(target_branch):
    try:
        output = subprocess.run(
            ["git", "merge-base", target_branch, "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        return output.stdout.strip()
    except subprocess.CalledProcessError:
        return ""

def git_modified_files(merge_base_sha):
    try:
        output = subprocess.run(
            ["git", "diff-index", "--name-only", "--diff-filter=M", merge_base_sha],
            capture_output=True,
            text=True,
            check=True
        )
        output = output.stdout.strip()
        return output.split("\n")
    except subprocess.CalledProcessError:
        return ""

def git_file_at_version(path, sha):
    try:
        output = subprocess.run(
            ["git", "--no-pager", "show", f"{sha}:{path}"],
            capture_output=True,
            text=True,
            check=True
        )
        return output.stdout.strip()
    except subprocess.CalledProcessError:
        return ""

def get_local_file(file):
    try:
        with open(file, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        return ""
    except Exception:
        return ""

def get_recent_prs(target_branch):
    github_repo_owner, github_repo_name = get_github_owner_repo()

    recent_prs_query = f"""
    query($github_repo_owner: String!, $github_repo_name: String!, $target_branch: String!) {{
        repository (owner: $github_repo_owner, name: $github_repo_name) {{
            pullRequests (first: 100, states: OPEN, baseRefName: $target_branch, orderBy: {{ field: CREATED_AT, direction: DESC }}) {{
                nodes {{
                    url
                    number
                    title
                    author {{ login }}
                    files (first: 100) {{ nodes {{ path }} }}
                    baseRefOid
                    headRef {{ target {{ oid }} }}
                }}
            }}
        }}
    }}
    """

    gh_cli_command = [
        "gh", "api", "graphql",
         "-F", f"github_repo_owner={github_repo_owner}",
         "-F", f"github_repo_name={github_repo_name}",
         "-F", f"target_branch={target_branch}",
         "-f", f"query={recent_prs_query}"
    ]

    try:
        output = subprocess.run(
            gh_cli_command,
            capture_output=True,
            text=True,
            check=True
        )
        output = output.stdout.strip()
        return dict(json.loads(output))
    except subprocess.CalledProcessError:
        return dict(json.loads("{}"))
