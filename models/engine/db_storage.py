#!/usr/bin/python3
"""This module defines a class to manage dbstorage for hbnb clone"""
import json


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """Returns a dictionary of models currently in storage"""
        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, pool_pre_ping=True)
        if HBNB_ENV == 'test':
            #Eliminar todas las tablas
