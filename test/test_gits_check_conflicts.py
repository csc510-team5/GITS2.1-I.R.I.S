import os
import sys

sys.path.insert(1, os.getcwd())

from gits_check_conflicts import modified_files, merge_base

def test_modified_files():
    target_branch = "master"
    merge_base_sha = merge_base(target_branch)
    files = modified_files(merge_base_sha)
    print(files)
    assert isinstance(files, list)