import subprocess

def get_github_owner_repo():
    try:
        output = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            capture_output=True,
            text=True,
            check=True
        )
        origin_url = output.stdout.strip().split('/')
        owner = origin_url[-2]
        repo = origin_url[-1][0:-4]
        return owner, repo
    except subprocess.CalledProcessError:
        return ""

