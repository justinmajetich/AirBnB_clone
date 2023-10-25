#!/bin/bash

# Check if pycodestyle is installed
if ! command -v pycodestyle; then
	  echo "Error: pycodestyle is not installed"
	    exit 1
fi

# Check all Python files in the current directory
for file in *.py; do
	  echo "Checking $file"
	    pycodestyle $file
    done

