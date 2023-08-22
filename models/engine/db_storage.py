#!/usr/bin/python3
"""
This module defines a class to manage
database storage for hbnb clone
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        # database connection details got from env variables
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        # create the engine
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
            pool_pre_ping=True)

        if getenv("HBNB_ENV ") == "test":
            # drop all tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in db storage"""
        dictionary = {}
        if cls is None:

            classes = [
                BaseModel, User, Place, State,
                City, Amenity, Review
            ]

            # for every class type of our system
            for cls in classes:
                # query to return all objects of type, cls in the db
                objects = self.__session.query(cls).all()

                # we save the returned objects in a dict of the form
                # key: <class-name>.<object-id>
                # value: object
                for object in objects:
                    key = f"{object.__class__.__name__}.{object.id}"
                    dictionary[key] = object
        else:
            # query to return all objects of the type, cls in the db
            objects = self.__session.query(cls).all()

            for object in objects:
                key = f"{object.__class__.__name__}.{object.id}"
                dictionary[key] = object

        return dictionary

    def new(self, obj):
        """Adds new object to db session"""
        self.__session.add(obj)

    def save(self):
        """Saves or persists data in session to the db"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from current db session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads the db and session"""
        # create all tables
        Base.metadata.create_all(self.__engine)

        # create the session
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
            """Close the session"""
            self.__session.remove()
