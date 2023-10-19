import os
import sys

sys.path.insert(1, os.getcwd())

from gits_check_conflicts import git_modified_files, git_merge_base, check_conflicts
from mock import patch, Mock

def test_modified_files():
    target_branch = "master"
    merge_base_sha = merge_base(target_branch)
    files = modified_files(merge_base_sha)
    print(files)
    assert isinstance(files, list)
 
@patch("subprocess.Popen") 
def test_check_conflicts_pass(mock_var):
    """
    Function to test gits check conflicts, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe
    test_result = check_conflicts()
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

    
@patch("subprocess.Popen") 
def test_check_conflicts_fail(mock_var):
    """
    Function to test gits check conflicts, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe
    test_result = check_conflicts()
    if test_result:
        assert True, "Normal Case"
    else:
        assert False

