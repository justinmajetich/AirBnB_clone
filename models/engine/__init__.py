"""
HBNB - A Holberton School Project for building a clone of Airbnb

This module contains the implementation of HBNB's data storage engine, which can store data either in a MySQL database or in JSON files.

Usage database:
    To use the MySQL database storage engine, set the environment variable HBNB_TYPE_STORAGE to 'db', and set the following environment variables to appropriate values for your MySQL installation:
    - HBNB_MYSQL_USER: the username for your MySQL user
    - HBNB_MYSQL_PWD: the password for your MySQL user
    - HBNB_MYSQL_HOST: the hostname of your MySQL server
    - HBNB_MYSQL_DB: the name of the MySQL database to use for HBNB storage

Usage JSON file:
    To use the JSON file storage just declare it, by default all your objects will be stored in a file called file.json

To interact with the data storage engine, import the storage module and call its methods, such as storage.all(), storage.new(obj), and storage.save().
"""
