#!/usr/bin/python3
"""
This module implements a Database Storage instance

# This class needs to be updated
"""
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import (
        sessionmaker,
        scoped_session
        )


class DBStorage():
    """
    Define the DBStorage engine

    * __engine : an sqlalchemy engine
    * __session: A session object to use for transactions
    * __env : A dictionary of environmental variables passed to the progam
    """
    __engine = None
    __session = None
    __env = None

    def __init__(self):
        """
        Initialize a DBStorage class
        """
        # Get environmental variables
        env_vars = [
                "HBNB_MYSQL_USER",
                "HBNB_MYSQL_PWD",
                "HBNB_MYSQL_HOST",
                "HBNB_MYSQL_DB"]

        self.__env = dict()

        self.__env.update({"HBNB_TYPE_STORAGE": getenv("HBNB_TYPE_STORAGE")})
        self.__env.update({"HBNB_ENV": getenv("HBNB_ENV")})

        for key in env_vars:
            value = getenv(key)

            # Ensure all environmental variables are valid
            if (value is None) and (self.__env["HBNB_TYPE_STORAGE"] == "db"):
                print("""** environmental variable '{}' is \
{} **""".format(key, value))
                print("""** Impossible to use {} \
**""".format(type(self).__name__))
                exit(1)

            else:
                # Update self.__env
                self.__env.update({key: value})

        # Add port to self.__env
        self.__env.update({"HBNB_MYSQL_PORT": 3306})

        # Create engine
        connection_url = "mysql+mysqldb://{}:{}@{}:{}/{}".format(
                self.__env["HBNB_MYSQL_USER"],
                self.__env["HBNB_MYSQL_PWD"],
                self.__env["HBNB_MYSQL_HOST"],
                self.__env["HBNB_MYSQL_PORT"],
                self.__env["HBNB_MYSQL_DB"])
        self.__engine = create_engine(connection_url, pool_pre_ping=True,
                                      echo=False)

        # Drop all tables if the envrionmental variable HBNB_ENV == "test"
        if self.__env["HBNB_ENV"] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Return all objects based on or not on the Class
        """
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.user import User
        from models.amenity import Amenity
        from models.review import Review

        classes = [City, State, Place, User, Amenity, Review]

        objs = list()
        if cls is None:
            for a_class in classes:
                objs = self.__session.query(a_class)\
                        .order_by(a_class.id)\
                        .all()
        elif cls in classes:
            objs = self.__session.query(cls)\
                    .order_by(cls.id)\
                    .all()

        # Modify objects so that the result will be dictionary of
        # key, value pais where
        # key = <class-name>.<object-id>
        # value = object
        dictionary = dict()
        for value in objs:
            key = type(value).__name__ + '.' + value.id
            dictionary.update({key: value})

        return dictionary

    def new(self, obj):
        """
        Add the object to the current database session
        """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Commit
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        SESSION CONFIGURATION
        ======================
        Create all tables if not existing and create a database session
        """
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.user import User
        from models.amenity import Amenity
        from models.review import Review

        # Create all tables
        Base.metadata.create_all(self.__engine)

        # Create current database session
        # The option expire_on_commit is False and
        # a scoped_session is used to ensure the Session is thread-safe
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)  # global scope

        Session = scoped_session(session_factory)
        self.__session = Session()
