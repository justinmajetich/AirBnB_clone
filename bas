#!/bin/bash

ROOT="/AirBnB_clone_v2"

files=$(find "$ROOT" -name "*.py")

for file in $files
do
    echo "Running pycodestyle on $file"
    pycodestyle "$file"
    echo "*NEXT FILE*"
done
