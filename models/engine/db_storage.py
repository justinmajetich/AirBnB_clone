#!/usr/bin/python3
"""Describes a database instance"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
import os

models = {"State": State, "City": City,
          "User": User, "Place": Place, "Review": Review}


class DBStorage:
    """Creates an database instance"""
    __engine = None
    __Session = None

    def __init__(self):
        """Instanciates attributes of the class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get('HBNB_MYSQL_USER'),
            os.environ.get('HBNB_MYSQL_PWD'),
            os.environ.get('HBNB_MYSQL_HOST'),
            os.environ.get('HBNB_MYSQL_DB'),
        ), pool_pre_ping=True)

        metadata = MetaData()

        if os.environ.get('HBNB_ENV') == 'test':
            # get existing tables from the db
            metadata.reflect(bind=self.__engine)

            # Iterate through all the tables
            for table in reversed(metadata.sorted_tables):
                table.drop(self.__engine)

    def all(self, cls=None):
        """Query the db for objs depending on cls name"""
        result = {}

        try:
            if cls is not None:
                cls = cls if type(cls) != str else models[cls]
                for obj in self.__Session.query(cls):
                    result[obj.__class__.__name__ + '.' + obj.id] = obj
            else:
                for mod in models:
                    for obj in self.__Session.query(models[mod]):
                        result[obj.__class__.__name__ + '.' + obj.id] = obj

        except Exception as e:
            print(f"Error querying the database: {e}")

        return result

    def new(self, obj):
        """Adds an object to the current session"""
        try:
            self.__Session.add(obj)
            # self.__Session.close()
        except Exception as e:
            print(f"Error adding object to session: {e}")

    def save(self):
        """commit all changes to the db session"""
        try:
            self.__Session.commit()
            # self.__Session.close()
        except Exception as e:
            print(f"Error committing changes to the database: {e}")

    def delete(self, obj=None):
        """Delete obj if from surrent db session"""
        try:
            if obj is not None:
                self.__Session.delete(obj)
        except Exception as e:
            print(f"Error deleting object from database")

    def reload(self):
        """Create tables if they don't exist
          Also create session
        """
        Base.metadata.create_all(self.__engine)
        Session_set = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__Session = scoped_session(Session_set)
