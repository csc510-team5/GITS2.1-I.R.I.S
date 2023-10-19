# About gits check conflicts

This command is used to check for merge conflicts between modified files in the current branch and pull requests made against a target branch.

# Location of Code

The code that implements the above mentioned gits functionality is located [here](https://github.com/csc510-team5/GITS2.1-I.R.I.S/blob/master/code/gits_check_conflicts.py).

# Code Description

## Functions

1. check_conflicts(args):
   this function checks for conflicts between local changes and pull requests by comparing modified files.

   Function prints the results of the modified file in a structured JSON format if conflicts are found. Otherwise the function returns.

2. git_merge_base(target_branch):
   this function takes **target_branch** as an input and retrieves the merge base commit between the current branch and the specified target branch.

   Function returns merge base commit's SHA as a string or an empty string if an error is encountered.

3. git_modified_files(merge_base_sha):
   this function takes **merge_base_sha** as input and returns a list of the files modified locally compared to the specified merge base commit.

   Function returns a list of file names that have been modified locally in the current branch compared to the specified merge base or am empty string if an error is encountered.

4. git_file_at_version(path, sha):
   this function takes in **path** and **sha** and retrieves the contents of the file with the given path at a patricular commit. The **path** argument represents the file path. The **sha** argument represents the SHA or commit hash of the commit at the file's content needs to be accessed.

   Function returnes the contents of the specified file or an empty string if an error is encountered.

5. get_local_file(file):
   this function takes in **file** and attempts to read the contents of the specified file from the local filesystem.

   Function returns the contents of the file if read successfully. An empty string is returned if the file does not exist or an error was encountered.

6. get_recent_prs(target_branch):
   this function takes in the **target_branch** argument and queries a GitHub repository to retrieve information about recent pull requests (PRs) with the specified target branch.

   Function returns a python dictionary of the information about the PRs or an empty dictionary if an error is encountered.

# How to run it? (Small Example)

Let say you are on a particular branch working on some feature X.
You want to compare your local changes to pull requests to check for merge conflicts.
You can use the following command to do so:

```
$ gits check_conflicts
```

