from subprocess import call


import os

TASK_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
BASH_SCRIPTS_DIR = "bash_scripts"


def cli():
    called = call('/'.join([TASK_ROOT_DIR, BASH_SCRIPTS_DIR, 'task_test.sh']))
