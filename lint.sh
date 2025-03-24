#!/bin/sh

set -e

echo "Formatting..."
echo "--- Ruff ---"
ruff format sportsfeatures
echo "--- isort ---"
isort sportsfeatures

echo "Checking..."
echo "--- Flake8 ---"
flake8 sportsfeatures
echo "--- pylint ---"
pylint sportsfeatures
echo "--- mypy ---"
mypy sportsfeatures
echo "--- Ruff ---"
ruff check sportsfeatures
echo "--- pyright ---"
pyright sportsfeatures
