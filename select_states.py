#!/usr/bin/python3
"""
Script that lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Establish connection to access the database and get the states
    from the database.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
