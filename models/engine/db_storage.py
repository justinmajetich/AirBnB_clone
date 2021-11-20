#!/usr/bin/python3
"""defines a class to manage database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


mapped_classes = (City, State)


class DBStorage:
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the storage"""
        usr = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            usr, pwd, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionaary of all objects in DB"""
        if cls:
            return {"{}.{}".format(cls.__name__, item.id): item
                    for item in self.__session.query(cls)}
        else:
            objs = {}
            for c in mapped_classes:
                objs.update({"{}.{}".format(c.__name__, item.id): item
                             for item in self.__session.query(c)})
            return objs

    def new(self, obj):
        """adds an object to the session"""
        self.__session.add(obj)

    def save(self):
        """commits the changes in  the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from the session"""
        if obj:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """reloads from the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
