# Python Bootcamp

* This python repos will set up the platform from which I've built a custom curriculum for myself.
* Mac specific

## Tooling

* Set up the python installer
  * [Setup pyenv](https://github.com/pyenv/pyenv#homebrew-in-macos)
    * follow the guide to install stuff
    * make sure to understand the cool commands
      * See the tools: `pyenv install --list`
      * Buy the tool: `pyenv install 3.7.0`
* Set up the virtualenv manager (optional)
  * [Setup pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
    * I've always used this. I think it's good to have just in case some scientist has anaconda or micropython
* Set up package manager/scaffolder
  * [Setup python-poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions)
    * Poetry requires Python 2.7 or 3.5+. It is multi-platform and the goal is to make it work equally well on Windows, Linux and OSX.
    * raspberry pi 3B+ uses 3.5.3
    * I use 3.7.0 for most things.
* Setup the command line
  * location: change directory to code folder
    * mkdir [project-name]
  * Have poetry detect the correct environment to shove into toml cargo file:
    * `pyenv local [3.7.0(whatever you want to use)]`
  * Confirm python version:
    * `python --versions`
* Scaffolding
  * `poetry new --src [PACKAGE_NAME]`
* Make sure vscode doesn't automatically activate a python environment for no reason
  * settings.json
    * set `"python.terminal.activateEnvironment": false,`
  * If you don't do this vscode will go ignore your python environment when you reopen your terminal within vscode.
* testing issues
---

## When Updating

* Dependencies
  * poetry toml change
    * go to the dependency and bump up
    * might need a poetry install (in the shell)
  * poetry lock change
* Updating python
  * in root `pyenv local [new version]`
  * poetry toml manual change
  * poetry lock change
    * `poetry lock` auto generates
* Keep in Minds
  * $HOME/Library/Caches/pypoetry/virtualenvs is where you have your virtualenvs
  * `poetry env info`
  * Upgrading within versions doesn't give you the requisite update in the env. poetry-demo-hash-py3.7 will not turn to poetry-demo-hash3.7.9, poetry reuses it.
  
## References

<https://github.com/Microsoft/vscode-python/issues/3066>

## NEED TO make scripts for these

* console out the requirements that poetry is doing in a ez to read manner
  * (no dev dependencies)
    * `poetry export --without-hashes | while IFS=  read -r line; do  echo $line | sed -e 's/;.*$//' ; done`
  * (with dev dependencies)
    * `poetry export --dev --without-hashes | while IFS=  read -r line; do  echo $line | sed -e 's/;.*$//' ; done`
  * my god , someone needs to make a task runner that does async io ops with python

## Questions

* <https://pypyr.io/> is this task running good?
