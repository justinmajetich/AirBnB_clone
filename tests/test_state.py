#!/usr/bin/python3
""" """
import MySQLdb

# connect to database
db = MySQLdb.connect(host="HBNB_MYSQL_HOST", user="HBNB_MYSQL_USER", passwd="HBNB_MYSQL_PWD", db="HBNB_MYSQL_DB")
cursor = db.cursor()

# get current number of records
cursor.execute("SELECT COUNT(*) FROM states")
num_records_before = cursor.fetchone()[0]

# execute console command to insert new record
console_command = "INSERT INTO states (column1, column2, column3) VALUES ('value1', 'value2', 'value3');"
cursor.execute(console_command)
db.commit()

# get number of records after insertion
cursor.execute("SELECT COUNT(*) FROM states")
num_records_after = cursor.fetchone()[0]

# check if difference is 1
if num_records_after - num_records_before == 1:
    print("Test Passed")
else:
    print("Test Failed")

# close database connection
db.close()
