import subprocess
import json

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

    conflicting_prs = [
        pr
        for pr in recent_prs
        if not set(modified_files).isdisjoint(pr.get('filePaths', []))
    ]
    if (not conflicting_prs):
        print("There are no conflicting pull requests!")
        return

    print(conflicting_prs)

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

def git_origin_url():
    try:
        output = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            capture_output=True,
            text=True,
            check=True
        )
        return output.stdout.strip()
    except subprocess.CalledProcessError:
        return ""

def get_recent_prs(target_branch):
    origin_url = git_origin_url()

    origin_url = origin_url.split('/')
    github_project_owner = origin_url[-2]
    github_project_name = origin_url[-1][0:-4]

    recent_prs_query = f"""
    query($github_project_owner: String!, $github_project_name: String!, $target_branch: String!) {{
        repository (owner: $github_project_owner, name: $github_project_name) {{
            pullRequests (first: 100, states: OPEN, baseRefName: $target_branch, orderBy: {{ field: CREATED_AT, direction: DESC }}) {{
                nodes {{
                    number
                    title
                    author {{ login }}
                    files (first: 100) {{ nodes {{ path }} }}
                    baseRef {{ target {{ oid }} }}
                    headRef {{ target {{ oid }} }}
                }}
            }}
        }}
    }}
    """

    gh_cli_command = [
        "gh", "api", "graphql",
         "-F", f"github_project_owner={github_project_owner}",
         "-F", f"github_project_name={github_project_name}",
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
