#!/bin/bash

# Array of server addresses
SERVER_ADDRESSES=("3.85.168.10" "54.146.78.93")

# Variables
SERVER_USERNAME="ubuntu"
SCRIPT_PATH="/home/max/alxprojects/AirBnB_clone_v2/0-setup_web_static.sh"
SSH_PRIVATE_KEY="/home/max/.ssh/school"

# Loop through server addresses
for SERVER_ADDRESS in "${SERVER_ADDRESSES[@]}"
do
  # SSH command to execute the remote script
 sudo  ssh -i ${SSH_PRIVATE_KEY} ${SERVER_USERNAME}@${SERVER_ADDRESS} 'bash -s' < ${SCRIPT_PATH} &
done

# Wait for all SSH sessions to finish
wait
