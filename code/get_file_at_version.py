import json
import requests
import subprocess
from urllib.parse import quote
from get_github_owner_repo import get_github_owner_repo

def get_file_at_version(path: str, sha: str) -> str:
    try:
        owner, repo = get_github_owner_repo()
        gh_cli_command = [
            "gh", "api", f"repos/{owner}/{repo}/contents/{quote(path)}?ref={sha}",
        ]
        output = subprocess.run(
            gh_cli_command,
            capture_output=True,
            text=True,
            check=True
        )
        output = output.stdout.strip()
        output = dict(json.loads(output))
        download_url = output["download_url"]

        content = ""
        response = requests.get(download_url);
        if response.status_code == 200:
            content = response.text
        return content
    except subprocess.CalledProcessError:
        return ""
