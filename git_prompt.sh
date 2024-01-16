#!/bin/bash

# Prompt the user for a commit message
read -p "Enter a commit message: " commit_message

# Add all changes to the staging area
git add .

# Commit changes with the provided commit message
git commit -m "$commit_message"

# Push changes to the remote repository
git push
