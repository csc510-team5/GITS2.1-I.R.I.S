import sys
import os

sys.path.insert(1, os.getcwd())

from get_github_owner_repo import get_github_owner_repo


def test_get_github_owner_repo():
    # Hardcoded for csc510-team5
    owner_name, repo_name = get_github_owner_repo()
    assert owner_name == 'csc510-team5'
    assert repo_name[:5] == 'GITS2.1-I.R.I.S'[:5]
