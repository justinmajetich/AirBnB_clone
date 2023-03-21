import MySQLdb
import os

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="hbnb_test",
                     passwd="hbnb_test_pwd",
                     db="hbnb_test_db")

# Create a cursor
cur = db.cursor()

# Get the number of current records in the table states
cur.execute("SELECT COUNT(*) FROM states")
count_before = cur.fetchone()[0]

# Execute the console command
os.system('echo "create State name=\\"California\\"" | ./console.py')

# Get the number of current records in the table states again
cur.execute("SELECT COUNT(*) FROM states")
count_after = cur.fetchone()[0]

# Close the cursor and database connection
cur.close()
db.close()

# Check if the difference is +1
assert (count_after - count_before) == 1
