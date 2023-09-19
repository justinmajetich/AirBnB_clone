#!/usr/bin/python3
""" This is the storage engine for the DB """
import os
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User

DB_NAME = getenv("HBNB_MYSQL_DB")
HOST = getenv("HBNB_MYSQL_HOST")
USERNAME = getenv("HBNB_MYSQL_USER")
PASSWORD = getenv("HBNB_MYSQL_PWD")
ENV = getenv("HBNB_ENV")


class DBStorage:
    """ A class representing the DB storage. """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializing instance """
        self.__engine = create_engine(
            f"mysql+mysqldb://{USERNAME}:{PASSWORD}@127.0.0.1/{DB_NAME}",
            pool_pre_ping=True
        )
        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns query based on class passed to it """
        classes = (City, State, User)
        all_objs: dict = {}

        if cls:
            # querying the class passed as arg.
            objects = self.__session.query(cls)
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                all_objs[key] = obj
        else:
            # If not i query all
            for item in classes:
                objects = self.__session.query(item).all()
                for obj in objects:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    all_objs[key] = obj
        return all_objs

    def new(self, obj):
        """ Add a new instance entry to the session """
        self.__session.add(obj)

    def save(self):
        """ Saves the instance to the db"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes the instance from the db """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates and reloads the database """
        Base.metadata.create_all(self.__engine)
        session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        ))
        self.__session = session()
