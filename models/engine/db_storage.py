#!usr/bin/python3
"""Defines a new class DBStorage"""
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DBStorage:
    """Describes a new class for Database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes new instance of DBStorage"""

        user = os.environ.get('HBNB_MYSQL_USER')
        passwd = os.environ.get('HBNB_MYSQL_PWD') 
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        env_check = os.environ.get('HBNB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}\
                                      @{host}:3306/{db}', pool_pre_ping=True)

        if env_check == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self):
        """Returns a list of specified Class or All classes"""
