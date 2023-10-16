import difflib
from typing import List, Iterable
import re


def get_common_modified_lines(gmr_old: List[str], gmr1_new: List[str], gmr2_new: List[str]) -> List[int]:
    # Normalize for different OS. Split lines into list, expected by difflib.united_diff
    gmr_old = normalize_line_endings(gmr_old).split('\n')
    gmr1_new = normalize_line_endings(gmr1_new).split('\n')
    gmr2_new = normalize_line_endings(gmr2_new).split('\n')
    
    # Generate unified diff patches for gmr_old to gmr1_new and gmr_old to gmr2_new
    gmr1_patch = difflib.unified_diff(gmr_old, gmr1_new, lineterm='', fromfile='a', tofile='b')
    gmr2_patch = difflib.unified_diff(gmr_old, gmr2_new, lineterm='', fromfile='a', tofile='b')

    # Get lists of modified lines from the generated patches
    gmr1_modified_lines = get_modified_lines(gmr1_patch)
    gmr2_modified_lines = get_modified_lines(gmr2_patch)

    # Find the common modified lines between gmr1 and gmr2
    return sorted(list(set(gmr1_modified_lines) & set(gmr2_modified_lines)))

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
