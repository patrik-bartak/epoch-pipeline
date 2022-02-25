# Epoch pipeline

Repository containing the pipeline intended to be used within Epoch.
Consists of pre-commit hooks and GitHub Actions pipeline.

## Pre-commit hook
Pre-commit hooks are managed using the `pre-commit` package.

### Running the hooks
Hooks are automatically run before any code is committed.
If a check fails or changes the contents of a file, the commit is aborted and the file changes must be checked and staged to commit again.
The following is checked:
- `check-yaml` verifies YAML syntax
- `check-yaml` verifies TOML syntax
- `end-of-file-fixer` makes sure files end in a newline
- `trailing-whitespace` trims trailing whitespace on lines
- `requirements-txt-fixer` sorts entries in requirements.txt
- `black` formats code according to PEP 8
- `pycln` removes unused imports
- `isort` sorts imports

For some packages, configurations can be changed in `pyproject.toml`.

### Adding new hooks
To add new hooks, change `.pre-commit-config.yaml` in the correct format and run `pre-commit install`.

### Updating

## GitHub Actions

that runs `Black` and automatically corrects major formatting mistakes. It also includes github actions including `flake8` and `isort` that run as a pipeline to check for things that `black` cannot.
- asdf
