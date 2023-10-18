import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_count_commits import count_commits
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_countcommits_sad_case(mock_var, mock_args):
    """
    Function to test gits countcommits, failure case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = count_commits(mock_args)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
