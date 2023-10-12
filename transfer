#!/usr/bin/env bash
# Transfers a file from our client to a server
#
# variables
path="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
filename=$(basename "$BASH_SOURCE")
file="$1"
ip="$2"
user="ubuntu"
key="~/.ssh/id_rsa"

if [ $# -eq 2 ]; then
        scp -i "$key" -o StrictHostKeyChecking=no "$path"/"$file" "$user"@"$ip":/home/"$user"/
else
        echo -e "Usage: $filename PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
fi
