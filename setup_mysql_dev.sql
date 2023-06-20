import mysql.connector

def prepare_mysql_server():
    # Connect to the MySQL server (assuming default host and port)
    connection = mysql.connector.connect(
        user = root
        password = root
    )

    "Create a cursor object to execute SQL queries"
    cursor = connection.cursor()

    "Create the database if it doesn't already exist"
    cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_dev_db")

    "Create the user if it doesn't already exist"
    cursor.execute("CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'")

    "Grant all privileges on hbnb_dev_db to hbnb_dev"
    cursor.execute("GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'")

    "Grant SELECT privilege on performance_schema to hbnb_dev"
    cursor.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'")

    "Flush privileges to apply the changes"
    cursor.execute("FLUSH PRIVILEGES")

    "Close the cursor and the connection"
    cursor.close()
    connection.close()

if __name__ == "__main__":
    prepare_mysql_server()

