# Advent of Code 2023

The goal of this project is to host my Advent of Code 2023 submissions. My goal for this year is to write each of the functions as TDD to see how much "easier" it is.

## Getting started

Ensure Poetry is installed on your path ex. `pip install poetry`. Then execute `poetry install` from the root directory to create your venv and install the requisite packages.

To create a new day from the cookiecutter template, execute `poetry run cookiecutter cc-template/` and follow the prompt. The cookiecutter template will create you a `main.py` file with an `execute` function which is the entry point. It also creates a test for that function automatically.

To execute the tests, run `poetry run pytest` to cover the entire suite, or execute a specific day by running `poetry run pytest Day_1`.

Ruff is included as a formatter and linter. To run these commands you can execute `poetry run ruff check .` and `poetry run ruff format .`.