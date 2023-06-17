#!/bin/bash

ROOT_DIR="/AirBnB_clone"

PYTHON_FILES=$(find "$ROOT_DIR" -name "*.py")

for FILE in $PYTHON_FILES
do
    echo "Running pycodestyle on $FILE"
    pycodestyle "$FILE"
done

