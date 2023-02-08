* This file tells us what all things we have to perform to set our project folder in local.
* Poetry Installation:
  1. Install the Poetry:  curl -sSL https://install.python-poetry.org | python
  2. Set the Environmental Variable
  3. poetry --version
* We have to create a poetry file (pyproject.toml) where we can put all the dependencies required for the project.
* To install the Dependency in poetry file (pyproject.toml): poetry install.  (It will create the poetry.lock file)
* To get the Virtual Env Details : poetry env info
* To Activate the Virtual Env : poetry shell
* To get the Allure report:
  1. add the command "--alluredir=`<path of the directory>`" to the python execution command.eg: python -m pytest -s -v tests\test_Login.py --browser Chrome --alluredir=reports
  2. allure serve `<path of the reports folder>`
     eg: allure serve reports
