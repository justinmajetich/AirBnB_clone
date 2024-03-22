#!/usr/bin/python3
"""
Model to manage DB storage using SQLAlchemy
"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


class DBStorage:
    """
    This class manages DB storage for AirBnb Clone using SQLAlchemy
    """
    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """
        Initializes __engine based on the Environment
        """
        # Code for __init__ method

    def all(self, cls=None):
        """Query on the current database session (self.__session)
        all objects depending on the class name"""
        # Code for all method

    def new(self, obj):
        """Creates a new instance in db storage"""
        # Code for new method

    def save(self):
        """Saves to the db storage"""
        # Code for save method

    def delete(self, obj=None):
        """Deletes obj from db storage"""
        # Code for delete method

    def reload(self):
        """Creates tables in database"""
        # Code for reload method

    def close(self):
        """Closing the session"""
        # Code for close method

