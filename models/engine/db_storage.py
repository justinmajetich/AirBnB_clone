#!/usr/bin/python3
""" This is the storage engine for the DB """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from models.base_model import Base
import models.misc as misc


class DBStorage:
    """ A class representing the DB storage. """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializing instance """
        try:
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
        except SQLAlchemyError as e:
            print(e)
            raise SQLAlchemyError

    def all(self, cls=None):
        """ Returns query based on class passed to it """
        try:
            all_objs: dict = {}

            if cls:
                objects = self.__session.query(cls)
                for obj in objects:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    all_objs[key] = obj
            else:
                for item in misc.classes.values():
                    objects = self.__session.query(item)
                    for obj in objects:
                        key = f"{obj.__class__.__name__}.{obj.id}"
                        all_objs[key] = obj
            return all_objs
        except SQLAlchemyError as e:
            print(e)
        finally:
            self.close()

    def new(self, obj):
        """ Add a new instance entry to the session """
        try:
            self.__session.add(obj)
        except SQLAlchemyError as e:
            print(e)
        finally:
            self.close()

    def save(self):
        """ Saves the instance to the db"""
        try:
            self.__session.commit()
        except SQLAlchemyError as e:
            print(e)
        finally:
            self.close()

    def delete(self, obj=None):
        """ Deletes the instance from the db """
        try:
            if obj:
                self.__session.delete(obj)
        except SQLAlchemyError as e:
            print(e)
        finally:
            self.close()

    def reload(self):
        """ Creates and reloads the database """
        try:
            Base.metadata.create_all(self.__engine)
            session = scoped_session(sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            ))
        except SQLAlchemyError as e:
            print(e)
        else:
            self.__session = session()

    def close(self):
        self.__session.close()
