#!/usr/bin/python3
"""New Engine DB_Storage"""

from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """New Engine DB_Storage"""

    __engine = None
    __session = None
    classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):

        db_parameters = {
            "host": getenv("HBNB_MYSQL_HOST"),
            "port": 3306,
            "user": getenv("HBNB_MYSQL_USER"),
            "pass": getenv("HBNB_MYSQL_PWD"),
            "db": getenv("HBNB_MYSQL_DB")
        }

        self.__engine = create_engine('mysql+mysqldb://{user}:{pass}@{host}:{port}/{db}'
                                      .format(**db_parameters), pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metada.drop_all(self.__engine)

    def all(self, cls=None):
        """return a dictionary with all objets of a class or all classes"""
        mydict = {}
        if cls is None:
            for myclass in self.classes:
                result = self.__session.query(myclass).all()
                for obj in result:
                    mydict[f"{obj.__class__}.{obj.id}"] = obj
        else:
            result = self.__session.query(cls).all()
            for obj in result:
                mydict[f"{obj.__class__}.{obj.id}"] = obj
        return mydict

    def new(self, obj):
        """ add the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy) """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
