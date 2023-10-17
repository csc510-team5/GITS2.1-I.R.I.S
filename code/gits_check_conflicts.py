import subprocess
import requests


def check_conflicts():
    target_branch = "master"
    merge_base_sha = merge_base(target_branch)
    files = modified_files(merge_base_sha)
    # call get_recent_gmrs
    # call parser
    
    
def merge_base(target_branch):
    try:
        output = subprocess.check_output(
            ["git", "merge-base", target_branch, "HEAD"]
        )
        return output.decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return None

def modified_files(merge_base_sha):
    try:
        output = subprocess.check_output(
            ["git", "diff-index", "--name-only", "--diff-filter=M", merge_base_sha]
        )
        return output.decode("utf-8").split("\n")
    except subprocess.CalledProcessError:
        return None
    
def get_recent_gmrs():
    target_branch = "main"
    graphql_url = "https://api.github.com/graphql"
    query = """
{
        repository(owner: "Trinea", name: "android-open-project") {
            pullRequests(first: 100,states: OPEN, orderBy: { field: CREATED_AT, direction: DESC }) {
                nodes {
                    number
                    title
                    author {
                        login
                    }
                    files(first: 100) {  # Adjust 'first' to limit the number of files retrieved
                        nodes {
                            path
                            additions
                            deletions


                        }
                    }
                    baseRef{
                        target{
                          oid
                        }
                    }
                    headRef{
                         target{
                          oid
                        }
                    }
                }
            }
        }
    }
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer Your-Git-Token",
    }

    data = {"query": query}
    response = requests.post(graphql_url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_data = response.json()  # Parse the JSON response
        print(json.dumps(response_data, indent=4))  # Print the response data with indentation


    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)
