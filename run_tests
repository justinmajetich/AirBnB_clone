#!/usr/bin/env bash
# Script to run python tests

if [ -s tests ]
then
	# run tests in interactive mode
	python3 -m unittest discover tests;
	# run tests in non interactive mode
	echo "python3 -m unittest discover tests" | bash
fi
