#!/usr/bin/python3
"""
This module contains some helper functions for the database storage test
"""
import MySQLdb


def run(command=None, statement=''):
    """
    run - execute a MySQLdb commmand
    command: the command to run on a cursor object example
        `cur.execute`

    If there is no statement, pass command as it is, example
        `cur.fetchall`
        Where, it actually means `cur.fetchall()`

    statement: The SQL statement to execute
    """
    return_value = None

    try:
        if (len(statement) == 0):
            return_value = command()
        else:
            return_value = command(statement)
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{:d}]: {:s}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {:s}".format(str(e)))

    return return_value
