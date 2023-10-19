import sys
import os

sys.path.insert(1, os.getcwd())

from parse_diff import normalize_line_endings, get_common_modified_lines


def test_normalize_line_endings():
    version1 = 'line1\r\nline2\r\nline3'
    version2 = 'line1\rline2\rline3'
    version3 = 'line1\nline2\nline3'
    
    assert normalize_line_endings(version1) == normalize_line_endings(version2) == normalize_line_endings(version3)
    
def test_common_modified_lines_modify_one_line_in_both():
    gmr_old = 'def f(a, b):\nreturn a + b'
    gmr1_new = 'def f(a, b):\nreturn a - b'
    gmr2_new = 'def f(a, b):\nc = 10\nreturn a/b'  # ignore "c = 10" addition
    
    assert get_common_modified_lines(gmr_old, gmr1_new, gmr2_new) == [2]
    
def test_common_modified_lines_modify_one_line_in_one():
    gmr_old = 'def f(a, b):\nreturn a + b'
    gmr1_new = 'def f(a, b):\nreturn a - b'
    gmr2_new = 'def f(a, b):\nc = 10\nreturn a + b'
    
    assert get_common_modified_lines(gmr_old, gmr1_new, gmr2_new) == []  # only gmr1 new was modified, not gmr2
    
def test_common_modified_lines_modify_multiple_line_in_both():
    gmr_old = 'def f(b):\na = 10\na = 7\nreturn a + b'
    gmr1_new = 'def f(b):\na = 5\na = 7\nreturn a - b'
    gmr2_new = 'def f(b):\na = 7\na = 10\n return a/b'  # ignore "c = 10" addition
    
    # NOT SURE IF THIS SHOULD BE CORRECT BECAUSE a IS REASSIGNED SO THE LOGIC IS DIFFERENT
    
    assert get_common_modified_lines(gmr_old, gmr1_new, gmr2_new) == [4]

def test_common_modified_lines_test_multiple_hunks():
    gmr_old = '1\n2\n3\n4\n5\n6\n9\n10\n11\n12\n13\n14\n17\n18\n19\n20\n21\n22'
    gmr1_new = '1\n2\n3\n4\n5\n7\n9\n10\n11\n12\n13\n15\n17\n18\n19\n20\n21\n23'
    gmr2_new = '1\n2\n3\n4\n5\n8\n9\n10\n11\n12\n13\n16\n17\n18\n19\n20\n21\n24'
    
    assert get_common_modified_lines(gmr_old, gmr1_new, gmr2_new) == [6, 12, 18]