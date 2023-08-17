#!/bin/bash

# Variables
SERVER="ubuntu@3.85.168.10"
ARCHIVE_PATH="versions/web_static_20230716023546.tgz"

# Copy the archive to the server
scp "$ARCHIVE_PATH" "$SERVER:/tmp/"

# Extract the archive on the server
ssh "$SERVER" "tar -xzf /tmp/$(basename "$ARCHIVE_PATH") -C /data/web_static/releases/"

# Update the symbolic link
ssh "$SERVER" "ln -sfn /data/web_static/releases/$(basename "$ARCHIVE_PATH" .tgz) /data/web_static/current"
