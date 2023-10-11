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

# Set the path to c7.sh in the same directory as this script
c7_script="$script_dir/c7.sh"

# Check if c7.sh exists
if [ ! -f "$c7_script" ]; then
    echo "Error: 'c7.sh' not found in the same directory as '$0'."
    exit 1
fi



# Set the "exit on error" option
set -e

# Run Task 7 script before executing Task 8
"$c7_script"

# Reset the "exit on error" option (optional, depending on your script)
set +e

rm place_id.txt

# Run Task 7 script before executing Task 8

echo ""
echo "--------------"
echo "--- TASK8 ---"
echo "--------------"
echo ""
# Retrieve City ID from the file
city_id=$(cat city_id.txt)
echo "#--> City ID: $city_id"
echo ""

# Retrieve User ID from the file
user_id=$(cat user_id.txt)
echo "#--> User ID: $user_id"
echo ""

# Create a new Place using the captured City ID and User ID
echo "#--> Creating a new Place with City ID: $city_id and User ID: $user_id..."
echo ""
place_output=$(echo 'create Place city_id="'$city_id'" user_id="'$user_id'" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297' | sudo -E HBNB_MYSQL_USER=$HBNB_MYSQL_USER HBNB_MYSQL_PWD=$HBNB_MYSQL_PWD HBNB_MYSQL_HOST=$HBNB_MYSQL_HOST HBNB_MYSQL_DB=$HBNB_MYSQL_DB HBNB_TYPE_STORAGE=$HBNB_TYPE_STORAGE "$console_path" | tee /dev/tty)
place_id=$(echo "$place_output" | grep -o -E '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}')
echo "#--> Place ID: $place_id"
echo ""

# List all Places
echo "#--> Listing all Places..."
echo ""
echo 'all Place' | sudo -E HBNB_MYSQL_USER=$HBNB_MYSQL_USER HBNB_MYSQL_PWD=$HBNB_MYSQL_PWD HBNB_MYSQL_HOST=$HBNB_MYSQL_HOST HBNB_MYSQL_DB=$HBNB_MYSQL_DB HBNB_TYPE_STORAGE=$HBNB_TYPE_STORAGE "$console_path"

echo ""
# Execute SQL query to list all Places
echo "#--> Executing SQL query to list all Places..."
echo ""
echo 'SELECT * FROM places\G' | sudo mysql -u$HBNB_MYSQL_USER -p$HBNB_MYSQL_PWD -h$HBNB_MYSQL_HOST $HBNB_MYSQL_DB

echo ""
# Save the Place ID to a file for reference
echo "$place_id" > place_id.txt
while [ ! -e place_id.txt ]; do
  sleep 1  # Wait for 1 second
done

echo ""