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
*
---

## References

<https://github.com/Microsoft/vscode-python/issues/3066>
