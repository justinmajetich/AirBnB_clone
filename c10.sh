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

# Set the path to setup_mysql_dev.sql
sql_path="$current_path/setup_mysql_dev.sql"

amenities="$current_path/main_place_amenities.py"

# Check if the required file exists
if [ ! -f "$sql_path" ]; then
    echo "#--> Error: 'setup_mysql_dev.sql' not found in '$current_path'."
    exit 1
fi
# Check if the required file exists
if [ ! -f "$amenities" ]; then
    echo "#--> Error: 'main_place_amenities.py' not found in '$current_path'."
    exit 1
fi
echo ""
echo "--------------"
echo "--- TASK10 ---"
echo "--------------"
echo ""
# Drop the hbnb_dev_db database if it exists
echo "#--> Dropping hbnb_dev_db database if it exists..."
echo ""
echo "DROP DATABASE IF EXISTS $HBNB_MYSQL_DB;" | sudo mysql -h$HBNB_MYSQL_HOST -u$YOUR_USER_MYSQL -p$YOUR_PASSWORD_MYSQL

echo ""
# Execute MySQL setup script
echo "#--> Executing MySQL setup script..."
echo ""
cat "$sql_path" | sudo mysql -h$HBNB_MYSQL_HOST -u$YOUR_USER_MYSQL -p$YOUR_PASSWORD_MYSQL

echo ""
# Set environment variables and run the Python script
echo "#--> Running main_place_amenities.py..."
echo ""
sudo -E HBNB_MYSQL_USER=$HBNB_MYSQL_USER \
    HBNB_MYSQL_PWD=$HBNB_MYSQL_PWD \
    HBNB_MYSQL_HOST=$HBNB_MYSQL_HOST \
    HBNB_MYSQL_DB=$HBNB_MYSQL_DB \
    HBNB_TYPE_STORAGE=$HBNB_TYPE_STORAGE \
    $amenities

echo ""
# Query amenities and places tables
echo "#--> Querying amenities table..."
echo ""
echo 'SELECT * FROM amenities\G' | sudo mysql -h$HBNB_MYSQL_HOST -u$HBNB_MYSQL_USER -p$HBNB_MYSQL_PWD $HBNB_MYSQL_DB

echo ""
echo "#--> Querying places table..."
echo ""
echo 'SELECT * FROM places\G' | sudo mysql -h$HBNB_MYSQL_HOST -u$HBNB_MYSQL_USER -p$HBNB_MYSQL_PWD $HBNB_MYSQL_DB

echo ""
echo "#--> Querying place_amenity table..."
echo ""
echo 'SELECT * FROM place_amenity\G' | sudo mysql -h$HBNB_MYSQL_HOST -u$HBNB_MYSQL_USER -p$HBNB_MYSQL_PWD $HBNB_MYSQL_DB

echo ""