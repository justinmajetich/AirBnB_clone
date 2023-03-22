#!/usr/bin/python3

# connect to the database

db = MySQLdb.connect(host="HBNB_MYSQL_HOST", user="HBNB_MYSQL_USER", password="HBNB_MYSQL_PWD", db="HBNB_MYSQL_DB")

args = 'State name="California"'

myclass = args[:args.find(' ')]

# close the database connection
db.close()
