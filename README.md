# Epoch pipeline

Repository containing the pipeline intended to be used within Epoch.
Consists of pre-commit hooks and GitHub Actions pipeline.

## Pre-commit hook
Pre-commit hooks are managed using the `pre-commit` package.

### Running the hooks
Hooks are automatically run before any code is committed.
If a check fails or changes the contents of a file, the commit is aborted and the file changes must be checked and staged to commit again.
The following is checked:
- `check-yaml` verifies YAML syntax (does not fix automatically)
- `check-yaml` verifies TOML syntax (does not fix automatically)
- `end-of-file-fixer` makes sure files end in a newline
- `trailing-whitespace` trims trailing whitespace on lines
- `requirements-txt-fixer` sorts entries in requirements.txt
- `black` formats code according to PEP 8
- `pycln` removes unused imports
- `isort` sorts imports

For some packages, configurations can be changed in `pyproject.toml`.

### Adding new hooks
To add new hooks, change `.pre-commit-config.yaml` in the correct format and run `pre-commit install`.

## GitHub Actions
GitHub Actions are used to set up a pipeline with `flake8`. This is a python linter and static analyzer that checks for more complicated issues, and therefore does not correct them automatically.
It is not necessary to pass `flake8` analysis for every commit, but it is necessary to pass the pipeline to merge pull requests.

This is set up in `.github > workflows > flake8.yaml`
