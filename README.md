# Poetry Python Project Template

![Static Badge](https://img.shields.io/badge/mission-A_useful_Python_poetry_template-blue)

[![Latest Tag](https://img.shields.io/github/v/tag/dylanhogg/poetry-python-project-template)](https://github.com/dylanhogg/poetry-python-project-template/tags)
[![Build](https://github.com/dylanhogg/poetry-python-project-template/workflows/build/badge.svg)](https://github.com/dylanhogg/poetry-python-project-template/actions/workflows/python-poetry-app.yml)
[![PyPI](https://badge.fury.io/py/poetry-python-project-template.svg)](https://badge.fury.io/py/poetry-python-project-template)

![Top language](https://img.shields.io/github/languages/top/dylanhogg/poetry-python-project-template)
![Last commit](https://img.shields.io/github/last-commit/dylanhogg/poetry-python-project-template)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dylanhogg/poetry-python-project-template/blob/master/notebooks/notebook.ipynb)

A quick-start [Poetry](https://python-poetry.org/) Python project template with helpful functionality and common libraries.

## Usage

- Ensure you rename all instances of `your_project_name` including the top level folder name.
- See the [Poetry docs](https://python-poetry.org/docs/cli/) for more information on using Poetry.

## Template Features

1. [Poetry](https://python-poetry.org/) for dependency management
1. Useful functionality wrapped in a `Makefile`
1. Helpful default packages (details below)
1. A GitHub CI build action using poetry that runs linting, type checking and unit tests
1. Example app showing logging and CLI arg parsing

## Application libraries included in template

1. [Python-dotenv](https://github.com/theskumar/python-dotenv) for environment variable management
2. [Typer](https://github.com/tiangolo/typer) for building CLI applications
3. [tqdm](https://github.com/tqdm/tqdm) for smart progress bar support
4. [Loguru](https://github.com/Delgan/loguru) for pleasant and powerful logging
5. [Rich](https://github.com/Textualize/rich) for beautiful terminal output

## Development libraries included in template

1. [pytest](https://github.com/pytest-dev/pytest) for writing your tests
2. [Black](https://github.com/psf/black) for code formatting
3. [Ruff](https://github.com/astral-sh/ruff) for fast linting and formatting
4. [pyright](https://github.com/microsoft/pyright) for static type checking
5. [coverage](https://github.com/nedbat/coveragepy) for code coverage
6. [pre-commit](https://github.com/pre-commit/pre-commit) for pre-commit hooks (black, ruff and pyright)
7. [pip-audit](https://github.com/pypa/pip-audit) for checking for security vulnerabilities

Happy templating!
