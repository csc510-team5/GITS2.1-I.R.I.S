import os
import sys

sys.path.insert(1, os.getcwd())

from gits_check_conflicts import git_modified_files, git_merge_base

def test_modified_files():
    target_branch = "master"
    merge_base_sha = git_merge_base(target_branch)
    files = git_modified_files(merge_base_sha)
    print(files)
    assert isinstance(files, list)
