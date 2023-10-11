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
sql_path="$current_path/setup_mysql_dev.sql"

# Check if the required files exist
if [ ! -f "$console_path" ]; then
    echo "#--> Error: 'console.py' not found in '$current_path'."
    exit 1
fi

if [ ! -f "$sql_path" ]; then
    echo "#--> Error: 'setup_mysql_dev.sql' not found in '$current_path'."
    exit 1
fi

# Get the directory where this script is located
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Set the path to c6.sh in the same directory as this script
c6_script="$script_dir/c6.sh"

# Check if c6.sh exists
if [ ! -f "$c6_script" ]; then
    echo "#--> Error: 'c6.sh' not found in the same directory as '$0'."
    exit 1
fi

# Set the "exit on error" option
set -e

# Run Task 6 script before executing Task 7
"$c6_script"

# Reset the "exit on error" option (optional, depending on your script)
set +e

rm user_id.txt
current_path=$(pwd)
echo ""
echo "--------------"
echo "--- TASK7 ---"
echo "--------------"
echo ""
# Create a new User and capture its ID
echo "#--> Creating a new User..."
echo ""
user_output=$(echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" last_name="Snow"' | sudo -E HBNB_MYSQL_USER=$HBNB_MYSQL_USER HBNB_MYSQL_PWD=$HBNB_MYSQL_PWD HBNB_MYSQL_HOST=$HBNB_MYSQL_HOST HBNB_MYSQL_DB=$HBNB_MYSQL_DB HBNB_TYPE_STORAGE=$HBNB_TYPE_STORAGE $console_path | tee /dev/tty)
user_id=$(echo "$user_output" | grep -o -E '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}')
echo "#--> User ID: $user_id"

echo ""
# List all Users
echo "#--> Listing all Users..."
echo ""
echo 'all User' | sudo -E HBNB_MYSQL_USER=$HBNB_MYSQL_USER HBNB_MYSQL_PWD=$HBNB_MYSQL_PWD HBNB_MYSQL_HOST=$HBNB_MYSQL_HOST HBNB_MYSQL_DB=$HBNB_MYSQL_DB HBNB_TYPE_STORAGE=$HBNB_TYPE_STORAGE $console_path

echo ""
# Execute SQL query to list all Users
echo "#--> Executing SQL query to list all Users..."
echo ""
echo 'SELECT * FROM users\G' | sudo mysql -h$HBNB_MYSQL_HOST -u$HBNB_MYSQL_USER -p$HBNB_MYSQL_PWD $HBNB_MYSQL_DB

echo ""
# Save the User ID to a file for Task 8
echo "$user_id" > user_id.txt
while [ ! -e user_id.txt ]; do
  sleep 1  # Wait for 1 second
done

echo ""