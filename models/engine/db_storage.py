#!/usr/bin/python3
"""
    This is the Database engine
    Author: Peter Ekwere
"""
from sqlalchemy import create_engine
from os.environ import getenv


class DBStorage:
    """ This Class will handle all data base storage """

    __engine = None
    __session = None
    
    user = getenv("HBNB_MYSQL_USER")
    password = getenv("HBNB_MYSQL_PWD")
    my_host = getenv("HBNB_MYSQL_HOST")
    database = getenv("HBNB_MYSQL_DB")

    def __init__(self):
        """ This is the DBStorage constructor """

