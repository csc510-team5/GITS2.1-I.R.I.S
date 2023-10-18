import gits_logging
import os
import sys
from pathlib import Path

def gits_list_commands(subparser_commands):
    """
    Function that prints list of custom commands
    to user console
    """
    print("GITS Custom Commands")

    for command in subparser_commands:
        print(f"gits {command}")

    path = ""
    if sys.platform[:3] == "win":
        path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)), "code")

    elif sys.platform == "linux" or sys.platform == "linux2":
        user_home_dir = str(Path.home())
        path = os.path.join(user_home_dir, "code")

    files = os.listdir(path)
    ignore_commands = ["logging"]
    default_commands = list(subparser_commands) + ignore_commands
    files = [file for file in files if file[5:-3] not in default_commands]

    for f in files:
        if "_" in f and "gits" in f:
            f = f.replace('_', ' ')
            f = f[0:-3]
            print(f)
    gits_logging.gits_logger.info("List of Custom Command ")
