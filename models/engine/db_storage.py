#!/usr/bin/python3
""" """
from ast import Delete
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
import urllib.parse


workspace = os.getenv("HBNB_ENV")
username = os.getenv("HBNB_MYSQL_USER")
passwd = urllib.parse.quote_plus(os.getenv("HBNB_MYSQL_PWD"))
host = os.getenv("HBNB_MYSQL_HOST") or "localhost"
port = 3306
db = os.getenv("HBNB_MYSQL_DB")
src = f"mysql+mysqldb://{username}:{passwd}@{host}:{port}/{db}"
Session = sessionmaker()


class DBStorage:
    """ This class manages storage of hbnb models in MySQL database """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor to initialize sqlalchemy sessions
            from the database connection
        """
        self.__engine = create_engine(src, pool_pre_ping=True)
        self.__session = Session.configure(bind=self.__engine)
        try:
            if workspace == "test":
                Base.metadata.drop_all(bind=self.__engine)
        except BaseException:
            pass

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dictionary = {}
        if cls:
            for obj in self.__session.query(cls):
                dictionary.update({f"{cls}.{obj.id}": obj.to_dict()})
        else:
            for obj in self.__session.query().all():
                dictionary.update({f"{cls}.{cls.id}": obj})
        return dictionary

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        scope = Session.configure(bind=self.__engine,
                                  expire_on_commit=False)
        self.__session = scoped_session(scope)

    def delete(self, obj=None):
        """ Deletes object from __objects """
        if obj:
            self.__session.delete(obj)
            self.save()
