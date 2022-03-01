from subprocess import call, check_call, run, PIPE


import os

TASK_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
BASH_SCRIPTS_DIR = "bash_scripts"


def cli():
    task_test = '/'.join([TASK_ROOT_DIR, BASH_SCRIPTS_DIR, 'task_test.sh'])
    # called = check_call(task_test)
    run(['sh', task_test], check=True)


# https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
'''
Prefer subprocess.run() over subprocess.check_call() and friends over subprocess.call() over subprocess.Popen() over os.system() over os.popen()
Understand and probably use text=True, aka universal_newlines=True.
Understand the meaning of shell=True or shell=False and how it changes quoting and the availability of shell conveniences.
Understand differences between sh and Bash
Understand how a subprocess is separate from its parent, and generally cannot change the parent.
Avoid running the Python interpreter as a subprocess of Python.
'''
