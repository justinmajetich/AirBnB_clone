#!/usr/bin/bash

# Drop the hbnb_dev_db database if it exists
echo "Dropping hbnb_dev_db database if it exists..."
echo "DROP DATABASE IF EXISTS hbnb_dev_db;" | sudo mysql
# Execute MySQL setup script

echo "Executing MySQL setup script..."
cat ./../../setup_mysql_dev.sql | sudo mysql


# Run the initial command and capture its output
output1=$(echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" last_name="Snow"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./../../console.py)

# Extract the UUID from the initial command's output using grep and awk
uuid1=$(echo "$output1" | grep -oE '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}' | awk '{print $1}')

# Check if the UUID is valid
if [ -n "$uuid1" ]; then
    echo "UUID from the initial command: $uuid1"
else
    echo "UUID not found in the output of the initial command."
    exit 1
fi

# Execute the subsequent command
output2=$(echo 'all User' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./../../console.py)

# Extract the UUID from the subsequent command's output
uuid2=$(echo "$output2" | grep -oE '\[User\] \([0-9a-fA-F\-]+\)' | grep -oE '[0-9a-fA-F\-]+')

# Check if the UUID from the subsequent command matches the initial UUID
if [ "$uuid1" == "$uuid2" ]; then
    echo "UUID from the subsequent command: $uuid2"
    echo "Both UUIDs match."
else
    echo "UUID from the subsequent command ($uuid2) does not match the initial UUID ($uuid1)."
    exit 1
fi

echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db
