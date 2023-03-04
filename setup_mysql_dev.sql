#!/usr/bin/python3
"""
script prepares a MySQL server for the project
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # MySQL configuration
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_host = 'localhost'
    mysql_db = None

    # Connect to MySQL server
    db = MySQLdb.connect(host=mysql_host,
                         user=mysql_username, passwd=mysql_password)

    # Create the database if it does not exist
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_dev_db;")
    cursor.execute("GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO\
     'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';")
    cursor.execute("GRANT SELECT ON performance_schema.* TO\
     'hbnb_dev'@'localhost';")
    cursor.close()
    db.close()

    print("MySQL server successfully prepared.")
