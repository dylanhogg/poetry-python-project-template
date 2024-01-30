# Poetry Python Project Template

[![Latest Tag](https://img.shields.io/github/v/tag/dylanhogg/poetry-python-project-template)](https://github.com/dylanhogg/poetry-python-project-template/tags)
[![Build](https://github.com/dylanhogg/poetry-python-project-template/workflows/build/badge.svg)](https://github.com/dylanhogg/poetry-python-project-template/actions/workflows/python-poetry-app.yml)

A quick-start [Poetry](https://python-poetry.org/) Python project template with helpful functionality and common libraries.

## Usage

- Ensure you rename all instances of `your_project_name` including the top level folder name.
- See the [Poetry docs](https://python-poetry.org/docs/cli/) for more information on using Poetry.

## Template Features

1. [Poetry](https://python-poetry.org/) for dependency management
1. Useful functionality wrapped in a `Makefile`
1. Helpful default packages (details below)
1. A GitHub build action
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
4. [coverage](https://github.com/nedbat/coveragepy) for code coverage
5. [pre-commit](https://github.com/pre-commit/pre-commit) for pre-commit hooks
6. [pip-audit](https://github.com/pypa/pip-audit) for checking for security vulnerabilities

Happy templating!
