#!/usr/bin/env bash
# code tester to be checked on each code change

# check the units tests passes
status_code="$(python3 -m unittest discover tests  2>&1 | tail -1)"
if [ "$status_code" == "OK" ]
then 
	echo  units tests OK
else
	echo "Unit tests $status_code"
	python3 -m unittest discover tests
	exit 1
fi

# check test the code in subfolders or /modules
# printout number of checks that failed

installed_="$(pip list |grep pycodestyle)"
if [ -z "$installed_" ]
then 
	pip install pycodestyle
else
	echo "pycodestyle is already installed"
fi

style_check="$(pycodestyle  */*.py *.py */*/*.py */*/*/*.py | wc -l )"
if  [ "$style_check" -gt 1 ]
then 
	echo "$style_check pycodestyle check failed"
	echo "$(pycodestyle  */*.py *.py */*/*.py)"
	exit 1
else
	echo "code style in models check passed"
fi

# self check test
#shell_check=shellcheck "$0"

