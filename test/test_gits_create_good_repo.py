import argparse
import sys
import os
import shutil
import pytest

sys.path.insert(1, os.getcwd())

from gits_create_good_repo import gits_create_good_repo
from mock import patch


def remove_extras(path):
    files = os.listdir(path)
    for file in files:
        if "py" in file:
            continue
        try:
            shutil.rmtree(file)
        except:
            os.remove(file)


@pytest.mark.skip(reason="gh has to be installed before testing this")
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(template="test_template"))
def test_gits_creategoodrepo(mockvar1):
    """
    Function to test gits creategoodrepo , success case
    """
    test_result = gits_create_good_repo(mockvar1)
    remove_extras(".")
    if test_result == 0:
        assert True, "Normal Case"
    else:
        assert False


@pytest.mark.skip(reason="gh has to be installed before testing this")
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(template=None))
def test_gits_creategoodrepo_novar_sadcase(mockvar1):
    """
    Function to test gits creategoodrepo without any args
    """
    test_result = gits_create_good_repo(mockvar1)
    remove_extras(".")
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False

# @patch("argparse.ArgumentParser.parse_args",
#        return_value=argparse.Namespace())
# # @patch("subprocess.Popen")
# def test_gits_creategoodrepo(mock_var1):
#     """
#     Function to test gits creategoodrepo , failure case i.e subprocess will return 1 on command failing to execute
#     """
#     mock_args = parse_args(mock_args)
#     test_result = gits_create_good_repo(mock_args)
#     remove_extras(".")
#     if test_result == 1:
#         assert True, "Failure Case - Success"
#     else:
#         assert False
