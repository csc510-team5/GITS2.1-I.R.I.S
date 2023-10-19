import difflib
from typing import List, Iterable
import re


def get_common_modified_lines(pr_old, pr1_new, pr2_new) -> List[int]:
    # Normalize for different OS. Split lines into list, expected by difflib.united_diff
    pr_old = pr_old.split('\n')
    pr1_new = pr1_new.split('\n')
    pr2_new = pr2_new.split('\n')
    
    # Generate unified diff patches for pr_old to pr1_new and pr_old to pr2_new
    pr1_patch = difflib.unified_diff(pr_old, pr1_new, lineterm='', fromfile='a', tofile='b')
    pr2_patch = difflib.unified_diff(pr_old, pr2_new, lineterm='', fromfile='a', tofile='b')

    # Get lists of modified lines from the generated patches
    pr1_modified_lines = get_modified_lines(pr1_patch)
    pr2_modified_lines = get_modified_lines(pr2_patch)

    # Find the common modified lines between pr1 and pr2
    return sorted(list(set(pr1_modified_lines) & set(pr2_modified_lines)))

def normalize_line_endings(text: str) -> str:
    # Normalize line endings to '\n'
    normalized_lines = re.sub(r'(\r\n|\r)', '\n', text)
    # Trim trailing whitespace
    normalized_lines = normalized_lines.rstrip()
    return normalized_lines

def get_modified_lines(patch: Iterable[str]) -> List[int]:
    modified_lines = []

    # Iterate through the lines in the patch
    for line in patch:
        if line.startswith('--- a'):  # skip header inserted by difflib.united_diff
            continue
        if line.startswith('@@ -'):
            old_start = int(line[4])
        if line.startswith('-'):
            # If the line starts with '-', it's considered a modified line in the old version
            modified_lines.append(old_start)
        if line.startswith(' ') or line.startswith('-'):
            # Update the old_start counter for non-added lines or modified lines
            old_start += 1

    return modified_lines
