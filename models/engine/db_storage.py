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
Base = declarative_base
class DatabaseStorage:
    """Database management of storage for hbnb clone"""
    __engine = None
    __session = None
    __tablename__ = 'states'
    def __init__(self):
        db_config = {
            'user': 'HBNB_MYSQL_USER',
            'password': 'HBNB_MYSQL_PWD',
            'host': 'HBNB_MYSQL_HOST',
            'database': 'HBNB_MYSQL_DB'
        }
        self.__engine = create_engine(f"mysql+mysqldb://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}", pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        session = self.__session()
        if cls is not None:
            objects = session.query(cls).all()
        else:
            objects = []
            queryclass = [User, State, City, Amenity, Place, Review]
            for queryclass in classes_to_query:
                    objects.extend(session.query(queryclass).all())
        session.close()
        return objects