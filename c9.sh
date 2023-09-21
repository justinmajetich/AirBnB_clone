#!/bin/bash

# Get the current working directory (path from where the script is called)
current_path=$(pwd)

config="$current_path/config.txt"
if [ ! -f "$config" ]; then
    echo "#--> Error: 'config.txt' not found in '$current_path'."
    exit 1
fi

# Read the configuration from config.txt
source $config

# Set the path to console.py and setup_mysql_dev.sql
console_path="$current_path/console.py"

# Check if the required files exist
if [ ! -f "$console_path" ]; then
    echo "#--> Error: 'console.py' not found in '$current_path'."
    exit 1
fi

# Get the directory where this script is located
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Set the path to c8.sh in the same directory as this script
c8_script="$script_dir/c8.sh"

# Check if c8.sh exists
if [ ! -f "$c8_script" ]; then
    echo "Error: 'c8.sh' not found in the same directory as '$0'."
    exit 1
fi



# Set the "exit on error" option
set -e

# Run Task 8 script before executing Task 9
"$c8_script"

# Reset the "exit on error" option (optional, depending on your script)
set +e


echo ""
echo "--------------"
echo "--- TASK9 ---"
echo "--------------"
echo ""
# Retrieve Place ID from the file
place_id=$(cat place_id.txt)
echo "#--> Place ID: $place_id"
echo ""

# Create a new User and capture its ID
echo "#--> Creating a new User..."
echo ""
user_output=$(echo 'create User email="bob@hbtn.io" password="bobpwd" first_name="Bob" last_name="Dylan"' | sudo -E HBNB_MYSQL_USER=$HBNB_MYSQL_USER HBNB_MYSQL_PWD=$HBNB_MYSQL_PWD HBNB_MYSQL_HOST=$HBNB_MYSQL_HOST HBNB_MYSQL_DB=$HBNB_MYSQL_DB HBNB_TYPE_STORAGE=$HBNB_TYPE_STORAGE $console_path | tee /dev/tty)
user_id=$(echo "$user_output" | grep -o -E '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}')
echo "#--> User ID: $user_id"


# Create a new Review using the captured Place ID and User ID
echo "#--> Creating a new Review with Place ID: $place_id and User ID: $user_id..."
echo ""
review_output=$(echo 'create Review place_id="'$place_id'" user_id="'$user_id'" text="Amazing_place,_huge_kitchen"' | sudo -E HBNB_MYSQL_USER=$HBNB_MYSQL_USER HBNB_MYSQL_PWD=$HBNB_MYSQL_PWD HBNB_MYSQL_HOST=$HBNB_MYSQL_HOST HBNB_MYSQL_DB=$HBNB_MYSQL_DB HBNB_TYPE_STORAGE=$HBNB_TYPE_STORAGE $console_path | tee /dev/tty)
review_id=$(echo "$review_output" | grep -o -E '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}')
echo "#--> Review ID: $review_id"
echo ""

# List all Reviews
echo "#--> Listing all Reviews..."
echo ""
echo 'all Review' | sudo -E HBNB_MYSQL_USER=$HBNB_MYSQL_USER HBNB_MYSQL_PWD=$HBNB_MYSQL_PWD HBNB_MYSQL_HOST=$HBNB_MYSQL_HOST HBNB_MYSQL_DB=$HBNB_MYSQL_DB HBNB_TYPE_STORAGE=$HBNB_TYPE_STORAGE $console_path

echo ""
# Execute SQL query to list all Reviews
echo "#--> Executing SQL query to list all Reviews..."
echo ""
echo 'SELECT * FROM reviews\G' | sudo mysql -u$HBNB_MYSQL_USER -p$HBNB_MYSQL_PWD -h$HBNB_MYSQL_HOST $HBNB_MYSQL_DB

echo ""