# Epoch pipeline

Repository containing the pipeline intended to be used within Epoch.
Consists of a pre-commit hook and GitHub Actions pipeline.

## Pre-commit hook
Before any code is committed, the following is run:
- `check-yaml` verifies YAML syntax
- `check-yaml` verifies TOML syntax
- `end-of-file-fixer` makes sure files end in a newline
- `trailing-whitespace` trims trailing whitespace on lines
- `requirements-txt-fixer` sorts entries in requirements.txt

## GitHub Actions

that runs `Black` and automatically corrects major formatting mistakes. It also includes github actions including `flake8` and `isort` that run as a pipeline to check for things that `black` cannot.
- asdf
