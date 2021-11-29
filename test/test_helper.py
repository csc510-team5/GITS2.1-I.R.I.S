# import os
# import sys

# sys.path.insert(1, os.getcwd())

# from helper import get_current_branch, get_repo_name
# from mock import patch, Mock


# @patch("subprocess.Popen")
# def test_get_repo_name_happy_case(mock_var):
#     """
#     Function to test fetching repo name and branch name, success case
#     """
#     mocked_pipe = Mock()
#     attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
#     mocked_pipe.configure_mock(**attrs)
#     mock_var.return_value = mocked_pipe

#     test_result = get_repo_name()
#     test_result_username = test_result[0][15:]
#     test_result_repo = test_result[1][:-4]
# #     assert "hrushabhchouhan" == test_result_username, "Normal case"
#     assert "testrepo" == test_result_repo, "Normal case"
    
    
# @patch("subprocess.Popen")
# def test_get_repo_name_happy_case_2(mock_var):
#     """
#     Function to test fetching repo name and user name, success case
#     """
#     mocked_pipe = Mock()
#     attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
#     mocked_pipe.configure_mock(**attrs)
#     mock_var.return_value = mocked_pipe

#     test_result = get_repo_name()

#     assert type(test_result[0]) == str, "Normal case"
#     assert type(test_result[1]) == str, "Normal case"


# @patch("subprocess.Popen")
# def test_get_repo_name_happy_case_3(mock_var):
#     """
#     Function to test fetching repo name and user name, success case
#     """
#     mocked_pipe = Mock()
#     attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
#     mocked_pipe.configure_mock(**attrs)
#     mock_var.return_value = mocked_pipe

#     test_result = get_repo_name()

#     assert type(test_result) == list, "Normal case"
    
    
# @patch("subprocess.Popen")
# def test_get_repo_name_sad_case(mock_var):
#     """
#     Function to test fetching repo name and branch name, failure case
#     """
#     mocked_pipe = Mock()
#     attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
#     mocked_pipe.configure_mock(**attrs)
#     mock_var.return_value = mocked_pipe

#     test_result = get_repo_name()
#     if not test_result:
#         assert False
#     else:
#         assert True
    
    
# @patch("subprocess.Popen")
# def test_get_current_branch_sad_case(mock_var):
#     """
#     Function to test fetching current branch, success case
#     """
#     mocked_pipe = Mock()
#     attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
#     mocked_pipe.configure_mock(**attrs)
#     mock_var.return_value = mocked_pipe

#     test_result = get_current_branch()
#     if not test_result:
#         assert True
#     else:
#         assert False


# @patch("subprocess.Popen")
# def test_get_trunk_branch_happy_case_master_branch(mock_var):
#     """
#     Function to test fetching main branch, success case when trunk branch='master'
#     """
#     mocked_pipe = Mock()
#     attrs = {'communicate.return_value': ('master'.encode('UTF-8'), 'error'), 'returncode': 0}
#     mocked_pipe.configure_mock(**attrs)
#     mock_var.return_value = mocked_pipe

#     test_result = get_current_branch()
#     assert "master" == test_result, "Normal case"


# @patch("subprocess.Popen")
# def test_get_trunk_branch_happy_case_main_branch(mock_var):
#     """
#     Function to test fetching main branch, success case when trunk branch='main'
#     """
#     mocked_pipe = Mock()
#     attrs = {'communicate.return_value': ('main'.encode('UTF-8'), 'error'), 'returncode': 0}
#     mocked_pipe.configure_mock(**attrs)
#     mock_var.return_value = mocked_pipe

#     test_result = get_current_branch()
#     assert "main" == test_result, "Normal case"


# @patch("subprocess.Popen")
# def test_get_trunk_branch_happy_case_other_branch(mock_var):
#     """
#     Function to test fetching main branch, success case when trunk branch is any other branch
#     """
#     mocked_pipe = Mock()
#     attrs = {'communicate.return_value': ('branch'.encode('UTF-8'), 'error'), 'returncode': 0}
#     mocked_pipe.configure_mock(**attrs)
#     mock_var.return_value = mocked_pipe

#     test_result = get_current_branch()
#     assert "branch" == test_result, "Normal case"


# @patch("subprocess.Popen")
# def test_get_trunk_branch_sad_case(mock_var):
#     """
#     Function to test fetching main branch, failure case
#     """
#     mocked_pipe = Mock()
#     attrs = {'communicate.return_value': ('branch', 'error'), 'returncode': 0}
#     mocked_pipe.configure_mock(**attrs)
#     mock_var.return_value = mocked_pipe

#     test_result = get_current_branch()
#     if not test_result:
#         assert True
#     else:
#         assert False
