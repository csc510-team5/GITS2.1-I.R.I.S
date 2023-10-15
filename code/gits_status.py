#!/usr/bin/python3

from subprocess import PIPE
import subprocess
import requests
import json


def gits_status(args):
    """
    Function that allows users to show status about
    1. changes present in the working directory but not in the staging area.
    2. changes present inside the staging area.
    3. changes to the files which are not being tracked.
    """
    try:
        status_cmd = ["git", "status"]
        process1 = subprocess.Popen(status_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        print(stdout.decode("UTF-8"))
        get_recent_gmrs()

    except Exception as e:
        print("ERROR: gits status command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True


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


