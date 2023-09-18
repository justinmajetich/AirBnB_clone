#!/usr/bin/env bash
# script to push code to github

if [ -z "$1" ] || [ -z "$2" ]
then
	echo "\$ Usage: ./push '<branch>' '<commit message>'"
else
	git add .
	git commit -m "$2";
	git push origin "$1";
fi
