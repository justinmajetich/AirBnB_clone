#!/usr/bin/python3
""" This is the storage engine for the DB """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import models.misc as misc


class DBStorage:
    """ A class representing the DB storage. """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializing instance """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                    misc.USERNAME,
                    misc.PASSWORD,
                    misc.HOST,
                    misc.DB_NAME
                ),
            pool_pre_ping=True
        )

        if misc.ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns query based on class passed to it """
        all_objs: dict = {}

        if cls:
            # querying the class passed as arg.
            objects = self.__session.query(cls)
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                all_objs[key] = obj
        else:
            # If not i query all
            for item in misc.classes.values():
                objects = self.__session.query(item)
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

    def close(self):
        self.__session.close()
