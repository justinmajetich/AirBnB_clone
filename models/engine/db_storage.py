#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in mysql database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance"""
        env = getenv('HBNB_ENV')
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        dialect = 'mysql'
        driver = 'mysqldb'

        self.__engine = create_engine("{}+{}://{}:{}@{}/{}".format(
            dialect, driver, user, pwd, host, db
        ), pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session all objects depending of the
        class name
        """
        classes = {
            'State': State,
            'City': City,
            'User': User,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

        objects = {}
        if cls and cls in classes:
            result = self.__session.query(classes[cls]).all()
            for obj in result:
                key = "{}.{}".format(cls, obj.id)
                objects[key] = obj
        else:
            for class_name, class_obj in classes.items():
                result = self.__session.query(class_obj).all()
                for obj in result:
                    key = "{}.{}".format(class_name, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        - Creates all tables in the database
        - Creates the current database session
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        )

    def close(self):
        """Closes the current SQLAlchemy session"""
        self.__session.close()
