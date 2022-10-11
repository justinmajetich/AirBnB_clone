#!/usr/bin/env bash


# remove all previously committed .pyc files from git
echo "Removing all tracked .pyc files"
find . -name "*.pyc" -exec git rm -f "{}" \;

# Fix pep8 errors with autopep8
echo "Running autopep..."
find -type f -name '*.py' ! -path '*/migrations/*' -exec autopep8 --in-place --aggressive --aggressive '{}' \;

# Run pycodestyle checker
echo "Running pycodestyle..."
find -type f -name '*.py' ! -path '*/migrations/*' -exec pycodestyle --first '{}' \;