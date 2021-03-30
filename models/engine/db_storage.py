#!/usr/bin/python3
""" This module creates an engine for saving to database """

class DBStorage:
        """ Class to run database engine """
        __engine = None
        __session = None

        __init__(self):
                """ Initializes class """