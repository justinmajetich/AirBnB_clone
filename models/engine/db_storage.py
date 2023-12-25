#!/usr/bin/python3
"""This module hosts the class DBStorage"""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.user import User


class DBStorage:
    """This class focuses in storing the objects in a MySQL database"""
    __engine = None
    __session = None
    __classes = [City, Place, Review, State, Amenity, User]

    def __init__(self):
        """create the engine (self.__engine)"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if (os.getenv('HBNB_ENV') == 'test'):
            for table in self.__engine.table_names():
                self.__engine.execute("DROP TABLE IF EXISTS {}".format(table))

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        if cls=None, query all types of objects(User, State, City,
        Amenity, Place and Review)
        this method must return a dictionary: where
        key = <class-name>.<object-id> and value = object
        """
        objects = {}
        if (cls):
            for obj in self.__session.query(cls.__name__).all():
                key = cls.__name__ + '.' + obj.id
                objects[key] = obj
        else:
            for elem in DBStorage.__classes:
                for obj in self.__session.query(elem).all():
                    key = elem.__name__ + '.' + obj.id
                    objects[key] = obj
        return objects

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.query(obj.__class__.__name__).get(obj.id).delete()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
