#!/usr/bin/python3
"""
Module Name:
db_storage

Module Description:
This module provides a storage engine for the HBNB project using SQLAlchemy to
connect to a MySQL database. The module contains only one class - DBStorage.

Module Classes:
- DBStorage: This is the main class of the module that provides methods
for creating, retrieving, updating, and deleting objects from the database.

Module Attributes:
- None
"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
    This class provides a storage
    engine for the HBNB project. The class uses SQLAlchemy to connect
    to a MySQL database and provides methods for creating, retrieving,
    updating, and deleting objects from the database.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        It initializes the database connection engine using the credentials
        stored in environment variables HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
        HBNB_MYSQL_HOST, and HBNB_MYSQL_DB. If the HBNB_ENV environment
        variable is set to "test", it drops all the tables in the database
        before creating them again.
        """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = \
            create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                    user,
                    password,
                    host,
                    database), pool_pre_ping=True)

        if (env == "test"):
            Base.metadata.drop_all(bind=self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls=None):
        """
        This method returns a dictionary containing all objects of a given
        class or all objects if no class is specified. It queries the database
        and returns a dictionary with keys in the format
        <class name>.<object id> and values set to the corresponding objects.
        It accepts a string as the cls parameter and converts it to the
        corresponding class using the built-in eval() function. If the cls
        parameter is not a string, it assumes it is a class and
        uses it directly.
        """
        value = {}
        if cls:
            for obj in self.__session.query(cls):
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                value[key] = obj
        else:
            for cls in [Amenity, City, Place, Review, State, User]:
                for obj in self.__session.query(cls):
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    value[key] = obj
        return value

    def new(self, obj):
        """
        This method adds the given object to the database session to be
        persisted later. It accepts an object as a parameter and adds
        it to the current session.
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        This method saves all pending changes to the database.
        It commits the current session to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        This method deletes the given object from the database.
        If no object is provided, it does nothing. If an object is provided,
        it deletes it from the current session.
        """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        This method creates all the tables defined in the models package using
        the SQLAlchemy create_all() function. It then creates a new session
        factory and binds it to the engine. Finally, it creates a new scoped
        session using the session factory and stores it in the __session
        attribute of the DBStorage object.
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def close(self):
        self.__session.close()
