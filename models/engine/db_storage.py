#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (create_engine)

from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __classes = [State, City, User, Place, Review, Amenity]
    __engine = None
    __session = None
    # SETUP RELATIONSHIP WITH City => State TODO

    def __init__(self):
        """init function for dbstorage to initialize engine and
            session with sqlalchemy
        """
        try:
            # build connection string
            user = os.environ.get('HBNB_MYSQL_USER')
            password = os.environ.get('HBNB_MYSQL_PWD')
            host = os.environ.get('HBNB_MYSQL_HOST')
            db = os.environ.get('HBNB_MYSQL_DB')
            env = os.environ.get('HBNB_ENV')
            mandatory = [user, password, host, db]
            # verify we got all neccessary attributes
            for attr in mandatory:
                if attr is None:
                    print("Missing mandatory env var")

            conn_str = "mysql+mysqldb://{}:{}@{}/{}".format(
                        user, password, host, db)
            # create engine and session object with connection string
            self.__engine = create_engine(conn_str, pool_pre_ping=True)

            # drop all tables in DB if test env
            if env == 'test':
                Base.metadata.drop_all(bind=self.__engine, checkfirst=True)
        except Exception as E:
            print("raised exception in init")
            print(E)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of objects stored in sqlalchemy
        """
        results = []
        if cls is None:
            for c in self.__classes:
                for result in self.__session.query(c):
                    results.append(result)
        else:
            result = self.__session.query(eval(cls))
            results = result.all()
        # return the results as a dictionary with class.id as key
        return {"{}.{}".format(result.__class__.__name__, result.id): result
                for result in results}

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj and self.__session:
            self.__session.add(obj)

    def save(self):
        """serialize the file path to JSON file path
        """
        if self.__session:
            self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from __objects if inside
        """
        try:
            self.__session.delete(obj)
        except:
            pass

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
            self.__session = scoped_session(session_factory)
        except Exception as E:
            print(E)

    def close(self):
        """removes our session"""
        self.__session.remove()
