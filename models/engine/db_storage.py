#!/usr/bin/python3

"""
Module for DBStorage class, which manages storage of
objects in a MySQL database.
"""

import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy import create_engine
from models import *


class DBStorage:
    """
    Class to manage storage of objects in a MySQL database.
    """
    __engine = None
    __session = None
    valid_classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):
        """
        Initializes DBStorage by creating a database engine and session.
        """
        self.__engine = create_engine("mysql+mysqldb://" +
                                      os.environ['HBNB_MYSQL_USER'] +
                                      ":" + os.environ['HBNB_MYSQL_PWD'] +
                                      "@" + os.environ['HBNB_MYSQL_HOST'] +
                                      ":3306/" +
                                      os.environ['HBNB_MYSQL_DB'])

        try:
            if os.environ['HBNB_MYSQL_ENV'] == "test":
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or specific class objects.
        Args:
            cls (str): Class name to filter objects.
        Returns:
            dict: Dictionary of objects (all or filtered by class).
        """
        storage = {}
        if cls is None:
            for cls_name in self.valid_classes:
                for instance in self.__session.query(eval(cls_name)):
                    storage[instance.id] = instance
        else:
            if cls not in self.valid_classes:
                return
            for instance in self.__session.query(eval(cls)):
                storage[instance.id] = instance

        return storage

    def new(self, obj):
        """
        Adds a new object to the database session.
        Args:
            obj: Object to be added.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits changes to the database session.
        """
        try:
            self.__session.commit()
        except:
            self.__session.rollback()
            raise
        finally:
            self.__session.close()

    def update(self, cls, obj_id, key, new_value):
        """
         Updates an object attribute value in the database.
         Args:
             cls (str): Class name of the object.
             obj_id (str): ID of the object.
             key (str): Attribute name to be updated.
             new_value: New value for the attribute.
         Returns:
             int: 1 if successful, 0 if object ID not found.
         """
        res = self.__session.query(eval(cls)).filter(eval(cls).id == obj_id)

        if res.count() == 0:
            return 0

        res.update({key: (new_value)})
        return 1

    def reload(self):
        """
        Creates all database tables and sets up a scoped session.
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def delete(self, obj=None):
        """
        Deletes an object from the database session.
        Args:
            obj: Object to be deleted.
        """
        if obj is None:
            return

        self.__session.delete(obj)

    def close(self):
        """
         Removes the session from the scope.
         """
        self.__session.remove()