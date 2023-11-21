#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
import os


class DBStorage:
    """Manages the storage of the content of the console into database """
    __engine = None
    __session = None

    def __init__(self):
        """Initialises the DBStorage Class"""
        self.__engine = create_engine('mysql+mysqldb://')
