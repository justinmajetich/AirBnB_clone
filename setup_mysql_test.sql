-- Creates a MySQL server with:
--   Database hbnb_test_db.
--   User hbnb_test with password hbnb_test_pwd in localhost.
--   Grants all privileges for hbnb_test on hbnb_test_db.
--   Grants SELECT privilege for hbnb_test on performance_schema.


-- Connect to the MySQL server as root (adjust the credentials if needed)
db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='your_root_password'
)

-- Create a cursor object to execute queries
cursor = db.cursor()

-- Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_test_db")

-- Create the user if it doesn't exist and set the password
cursor.execute("CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd'")

-- Grant all privileges on hbnb_test_db to hbnb_test
cursor.execute("GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost'")

-- Grant SELECT privilege on performance_schema to hbnb_test
cursor.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'")

-- Flush privileges to apply the changes
cursor.execute("FLUSH PRIVILEGES")

-- Close the cursor and database connection
cursor.close()
db.close()
