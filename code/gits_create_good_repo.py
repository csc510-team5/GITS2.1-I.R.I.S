"""
To clone from a template repo, we need to run the following commands:

We have created a new template repo already with some pre-defined files that encompass the structure of a good repo.

Cloning from the template can be done with:
gh repo create <repo name> --template sak007/goodRepo_template --public -y

git clone https://github.com/sak007/goodRepo_template.git

git init --template ./goodRepo_template

"""

# from subprocess import Popen, PIPE
import subprocess
import gits_logging
import sys


def gits_create_good_repo(args):
    try:
        print("1. Apache\n2. MIT\n3. GNU\n")
        license = int(input("Enter License(a number from 1-3):"))
        if license == 1:
            process_commands = ["gh", "repo", "create", args.repo_name, "--template", "sak007/goodRepo_template", "--public", "-y"]
        elif license == 2:
            process_commands = ["gh", "repo", "create", args.repo_name, "--template", "nehaAgarwal96/goodRepo_template2", "--public", "-y"]
        elif license == 3:
            process_commands = ["gh", "repo", "create", args.repo_name, "--template", "hrushabhchouhan/goodRepo_template3", "--public", "-y"]
        else:
            process_commands = ["gh", "repo", "create", args.repo_name, "--template", "sak007/goodRepo_template", "--public", "-y"]

        if sys.platform == "linux" or sys.platform == "linux2":
            process = subprocess.Popen(process_commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if(process.returncode == 1):
                return False
        elif sys.platform[:3] == "win":
            process = subprocess.Popen(process_commands, shell=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if(process.returncode == 1):
                return False
    except Exception as e:
        gits_logging.gits_logger.error(
            "gits creategoodrepo command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits creategoodrepo command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
