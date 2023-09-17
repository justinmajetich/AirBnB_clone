#!/bin/bash

# Drop the hbnb_dev_db database if it exists
echo "Dropping hbnb_dev_db database if it exists..."
echo "DROP DATABASE IF EXISTS hbnb_dev_db;" | sudo mysql
# Execute MySQL setup script

echo "Executing MySQL setup script..."
cat ./../../setup_mysql_dev.sql | sudo mysql

# Create a new State and capture its ID
echo "Creating a new State..."
state_output=$(echo 'create State name="California"' | sudo -E HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./../../console.py)
state_id=$(echo "$state_output" | grep -o -E '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}')
echo "State ID: $state_id"

# List all States
echo "Listing all States..."
echo 'all State' | sudo -E HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./../../console.py

# Execute SQL query to list all States
echo "Executing SQL query to list all States..."
echo 'SELECT * FROM states\G' | sudo mysql -uhbnb_dev -phbnb_dev_pwd hbnb_dev_db

# Create a new City with the captured State ID
echo "Creating a new City with State ID: $state_id..."
echo "create City state_id=\"$state_id\" name=\"San_Francisco\"" | sudo -E HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./../../console.py

# List all Cities
echo "Listing all Cities..."
echo 'all City' | sudo -E HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./../../console.py

# Create another City with the captured State ID
echo "Creating another City with State ID: $state_id..."
echo "create City state_id=\"$state_id\" name=\"San_Jose\"" | sudo -E HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./../../console.py

# Execute SQL query to list all Cities
echo "Executing SQL query to list all Cities..."
echo 'SELECT * FROM cities\G' | sudo mysql -uhbnb_dev -phbnb_dev_pwd hbnb_dev_db
