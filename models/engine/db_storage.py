#!/usr/bin/python3
"""Database storage engine using SQLAlchemy with a mysql+mysqldb database
connection.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine and session for database storage."""
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        db = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db}',
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

        Session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        ))
        self.__session = Session()

    def all(self, cls=None):
        """Query and return objects from the current database session.
        """
        query_result = {}

        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes_to_query = [User, State, City, Amenity, Place, Review]
            objects = []
            for cls in classes_to_query:
                objects.extend(self.__session.query(cls).all())

        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            query_result[key] = obj

        return query_result

    def new(self, obj):
        """Add an object to the session."""

        self.__session.add(obj)

    def save(self):
        """Commit changes to the database."""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the session."""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload data from the database."""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        ))()
