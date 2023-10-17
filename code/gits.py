# /usr/bin/python3

import sys
import argparse
from gits_logging import init_gits_logger
from gits_hello import gits_hello
from gits_add import gits_add_func
from gits_commit import gits_commit_func
from gits_set import gits_set_func
from gits_setupstream import upstream
from gits_create_branch import create_branch
from gits_super_reset import super_reset

from gits_rebase import gits_rebase
from gits_reset import gits_reset
from gits_delete import gits_delete

from gits_profile import gits_set_profile
from gits_track import gits_track
from gits_untrack import gits_untrack
from gits_undo import gits_undo
from gits_sync import gits_sync
from gits_push import gits_push
from gits_switch import switch_branch
from gits_merge import merge_branch
from gits_status import gits_status
from gits_diff import gits_diff
from gits_branch import gits_branch
from gits_init import gits_init
from gits_pull import gits_pull
from gits_creategoodrepo import gits_creategoodrepo
from gits_custom import gits_custom
from gits_list import gits_list_commands
from gits_version import gits_version
from gits_countcommits import count_commits
from gits_check_conflicts import check_conflicts 

from gits_auth import gits_authenticator

logger_status = init_gits_logger()
if not logger_status:
    print("ERROR: logger not initialised")
    sys.exit(1)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_hello_subparser = subparsers.add_parser('hello')
gits_hello_subparser.set_defaults(func=gits_hello)

gits_auth_subparser = subparsers.add_parser('auth')
# gits_auth_subparser.add_argument("method", help="Method: Either use --web or --with-token")
gits_auth_subparser.set_defaults(func=gits_authenticator)

gits_set_subparser = subparsers.add_parser('set')
gits_set_subparser.add_argument('--parent', help='git parent branch')
gits_set_subparser.set_defaults(func=gits_set_func)

gits_add_subparser = subparsers.add_parser('add')
gits_add_subparser.add_argument('file_names',
                                metavar='N',
                                type=str,
                                nargs='+',
                                help='all file names')
gits_add_subparser.set_defaults(func=gits_add_func)

gits_commit_subparser = subparsers.add_parser('commit')
gits_commit_subparser.add_argument('-m',
                                   required=True,
                                   help='git commit message')
gits_commit_subparser.add_argument('--amend',
                                   action='store_true',
                                   help='amend commit message')
gits_commit_subparser.set_defaults(func=gits_commit_func)

gits_create_subparser = subparsers.add_parser('create')
gits_create_subparser.add_argument('-b', help="branch name to create")
gits_create_subparser.set_defaults(func=create_branch)

gits_switch_subparser = subparsers.add_parser('switch')
gits_switch_subparser.add_argument('branch_name', help="branch name to switch")
gits_switch_subparser.set_defaults(func=switch_branch)

gits_merge_subparser = subparsers.add_parser('merge')
gits_merge_subparser.add_argument('branch_name', help="branch name to merge")
gits_merge_subparser.set_defaults(func=merge_branch)

gits_upstream_subparser = subparsers.add_parser('upstream')
gits_upstream_subparser.add_argument('--remote',
                                     help='the remote branch name')
gits_upstream_subparser.add_argument('--local',
                                     help="local branch name")
gits_upstream_subparser.add_argument('--upstream',
                                     help="the upstream branch name")
gits_upstream_subparser.set_defaults(func=upstream)

gits_profile_subparser = subparsers.add_parser('profile', help='profie help')
gits_profile_subparser.set_defaults(func=gits_set_profile)
gits_profile_subparser.add_argument('--email',
                                    required=True,
                                    help='email to be used')
gits_profile_subparser.add_argument('--name',
                                    required=True,
                                    help='name to be used')

gits_super_reset_subparser = subparsers.add_parser('super-reset')
gits_super_reset_subparser.add_argument('--name',
                                        help="Name of the repository to super reset")
gits_super_reset_subparser.set_defaults(func=super_reset)

gits_rb_subparser = subparsers.add_parser('rebase', help='sync help')
gits_rb_subparser.set_defaults(func=gits_rebase)

gits_status_subparser = subparsers.add_parser('status', help='sync help')
gits_status_subparser.set_defaults(func=gits_status)

gits_diff_subparser = subparsers.add_parser('diff', help='sync help')
gits_diff_subparser.set_defaults(func=gits_diff)

gits_branch_subparser = subparsers.add_parser('branch', help='sync help')
gits_branch_subparser.set_defaults(func=gits_branch)

gits_reset_subparser = subparsers.add_parser('reset', help='sync help')
gits_reset_subparser.set_defaults(func=gits_reset)
gits_reset_subparser.add_argument(
    '--branch', required=True, help='branch to be used')

gits_reset_subparser = subparsers.add_parser('delete', help='sync help')
gits_reset_subparser.set_defaults(func=gits_delete)
gits_reset_subparser.add_argument(
    '--branch', required=True, help='branch to be used')
gits_reset_subparser.add_argument(
    '--count', required=True, help='Last commits to be deleted')

gits_track_subparser = subparsers.add_parser('track')
gits_track_subparser.add_argument('file_names',
                                  metavar='N',
                                  type=str,
                                  nargs='+',
                                  help='all file names')
gits_track_subparser.set_defaults(func=gits_track)

gits_untrack_subparser = subparsers.add_parser('untrack')
gits_untrack_subparser.add_argument('file_names',
                                    metavar='N',
                                    type=str,
                                    nargs='+',
                                    help='all file names')
gits_untrack_subparser.set_defaults(func=gits_untrack)

gits_undo_subparser = subparsers.add_parser('undo')
gits_undo_subparser.add_argument('file_names',
                                 metavar='N',
                                 type=str,
                                 nargs='+',
                                 help='all file names')
gits_undo_subparser.set_defaults(func=gits_undo)

gits_sync_subparser = subparsers.add_parser('sync')
gits_sync_subparser.add_argument('-source', help="name of the trunk branch")
gits_sync_subparser.set_defaults(func=gits_sync)

gits_push_subparser = subparsers.add_parser('push')
gits_push_subparser.add_argument("--rebase", nargs=1, default=False,
                                 help="do a pull rebase before pushing the changes",
                                 required=False)
gits_push_subparser.set_defaults(func=gits_push)

gits_init_subparser = subparsers.add_parser("init")

gits_init_subparser.add_argument("--bare", action="store_true",
                                 help="intialize an empty git repositories but omit the working directory")
gits_init_subparser.add_argument(
    "--template", help="initialize a git repository using predifined templates")
gits_init_subparser.add_argument(
    "--clone_url", help="url for cloning an already existing repo")
gits_init_subparser.set_defaults(func=gits_init)

gits_pull_subparser = subparsers.add_parser("pull")
gits_pull_subparser.add_argument("--nocommit", action='store_true',
                                 help="fetches the remote contain but does not create a new merge commit",
                                 required=False)
gits_pull_subparser.add_argument("--rebase", action='store_true',
                                 help="uses git rebase to merge with the remote branch",
                                 required=False)
gits_pull_subparser.add_argument("--branch", nargs="?", default=False,
                                 help="you can specify the branch you want to pull",
                                 required=False)
gits_pull_subparser.set_defaults(func=gits_pull)

gits_countcommits_subparser = subparsers.add_parser("countcommits")
gits_countcommits_subparser.set_defaults(func=count_commits)

gits_list_subparser = subparsers.add_parser("list")
gits_list_subparser.set_defaults(func=gits_list_commands)

gits_version_subparser = subparsers.add_parser("version")
gits_version_subparser.set_defaults(func=gits_version)

gits_creategoodrepo_subparser = subparsers.add_parser("creategoodrepo")
gits_creategoodrepo_subparser.add_argument("repo_name", help="name of the repo")
gits_creategoodrepo_subparser.set_defaults(func=gits_creategoodrepo)

gits_check_conflicts_subparser = subparsers.add_parser("check_conflicts")
gits_check_conflicts_subparser.set_defaults(func=check_conflicts)

gits_custom_subparser = subparsers.add_parser("custom")
gits_custom_subparser.add_argument(
    "command",
    help="command to be used to execute sequence of custom commands"
)
gits_custom_subparser.add_argument(
    "--create", action='store_true',
    help="create a new custom command",
    required=False
)
gits_custom_subparser.add_argument(
    "-c", action='store_true',
    help="create a new custom command",
    required=False
)
gits_custom_subparser.add_argument(
    "--update", action='store_true',
    help="update the existing custom command",
    required=False
)
gits_custom_subparser.add_argument(
    "-u",
    action='store_true',
    help="update the existing custom command",
    required=False
)
gits_custom_subparser.add_argument(
    "--delete",
    action='store_true',
    help="delete a custom command",
    required=False
)
gits_custom_subparser.add_argument(
    "-d",
    action='store_true',
    help="delete a custom command",
    required=False
)
gits_custom_subparser.set_defaults(func=gits_custom)

args = parser.parse_args()
args.func(args)
