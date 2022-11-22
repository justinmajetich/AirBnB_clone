#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

import MySQLdb
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
import os

__engine = None
__session = None

def __init__(self):
    # Return the value of the environment variable key as a string if it exists
    self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(os.getenv("HBNB_MYSQL_USER"), os.getenv("HBNB_MYSQL_PWD"), os.getenv("HBNB_MYSQL_HOST"), os.getenv("HBNB_MYSQL_DB")),
    pool_pre_ping=True)

    # drop all tables if the environment variable HBNB_ENV is equal to test
    if os.getenv("HBNB_ENV") == "test":
        Base.metadata.drop_all(__engine)

def all(self, cls=None):
    self.__session.query(cls).all()

    if cls == None:

