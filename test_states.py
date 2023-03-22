#!/usr/bin/python3
""" """
import MySQLdb

# Open database connection
db = MySQLdb.connect("hostname", "username", "password", "database_name")

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to get count of records in states table
sql = "SELECT COUNT(*) FROM states"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch the result
    result = cursor.fetchone()
    # Print the count of records in the states table
    print("Number of records in the 'states' table:", result[0])
except:
    print("Error: Unable to fetch data.")

# Close the database connection
db.close()
