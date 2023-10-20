import os
import sys

sys.path.insert(1, os.getcwd())

from gits_check_conflicts import git_modified_files, git_merge_base

def test_modified_files():
    target_branch = "master"
    merge_base_sha = git_merge_base(target_branch)
    files = git_modified_files(merge_base_sha)
    assert isinstance(files, list)

def test_modified_files_for_non_existing_branch():
    #branch name with space is not a valid branch
    target_branch = "my invalid branch"
    merge_base_sha = git_merge_base(target_branch)
    files = git_modified_files(merge_base_sha)
    assert len(files) == 0





