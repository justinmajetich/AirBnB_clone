#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class DatabaseStorage:
    """Database management of storage for hbnb clone"""
    __engine = None
    __session = None
    def __init__(self):
        db_config = {
            'user': 'HBNB_MYSQL_USER',
            'password': 'HBNB_MYSQL_PWD',
            'host': 'HBNB_MYSQL_HOST',
            'database': 'HBNB_MYSQL_DB'
        }
        self.__engine = create_engine(f"mysql+mysqldb://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}", pool_pre_ping=True)
