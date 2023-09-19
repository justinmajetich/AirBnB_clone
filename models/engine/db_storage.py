#!/usr/bin/python3
"""
Defining the db storage for the project
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.state import State
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):

        db_user = os.environ.get("HBNB_MYSQL_USER")
        db_password = os.environ.get("HBNB_MYSQL_PWD")
        db_host = os.environ.get("HBNB_MYSQL_HOST")
        db_name = os.environ.get("HBNB_MYSQL_DB")
        db_env = os.environ.get("HBNB_ENV")

        db_url = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}/{db_name}"

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if db_env == "test":
            self.__engine.execute("DROP DATABASE IF EXISTS hbnb_test_db")
            self.__engine.execute("CREATE DATABASE IF NOT EXISTS hbnb_test_db")
            self.__engine.execute("USE hbnb_test_db")

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        objects_dict = {}
        if cls is None:
            classes_to_query = [User, State, City, Amenity, Place, Review]
        else:
            classes_to_query = [cls]

        for class_type in classes_to_query:
            objects = self.__session.query(class_type).all()
            for obj in objects:
                key = f"{class_name}.{obj.id}"
                objects_dict[key] = obj

        return objects_dict

    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and create the
        current database session.
        """

        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(Session)
