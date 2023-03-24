#!/usr/bin/python3
"""This module defines a class to manage DBstorage"""
import MySQLdb
import os
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = "None"
    __session = "None"

    def __init__(self):

        # Retrieve the value of the "HBNB_MYSQL_USER" environment variable
        self.user = os.environ.get("HBNB_MYSQL_USER")
        self.password = os.environ.get("HBNB_MYSQL_PWD")
        # Retrieve the value of the "HBNB_MYSQL_HOST" environment variable with
        # a default value
        self.host = os.environ.get("HBNB_MYSQL_HOST", "localhost")
        self.database = os.environ.get("HBNB_MYSQL_DB")

        db_url = (f"mysql+mysqldb://{self.user}:{self.password}@{self.host}/{self.database}")
        self.__engine = create_engine(db_url, echo=True, pool_pre_ping=True)
        # self.__engine = create_engine(db_url)
        # scoped_session to ensure thread_safety when creates a new database
        # session
        self.Session = scoped_session(sessionmaker(bind=self.__engine,
            expire_on_commit=False))

        if os.getenv("HBNB_ENV") == "test":
            print("test env")
            db_url = (f"mysql+mysqldb://{self.user}:{self.password}@{self.host}/{self.database}")
            engine = create_engine(db_url, pool_pre_ping=True)
            metadata = MetaData(bind=engine)
            metadata.reflect(engine)
            metadata.drop_all()

    def all(self, cls=None):
        objects = {}
        results = self.__engine.execute(select(cls))
        results = [cls(**dict(zip(row.keys(), row))) for row in results.all()]
        for r in results:
            objects[f"{cls.__name__}.{r.id}"] = r
        return objects

        c = self.__engine.cursor()
        query = ("SELECT * FROM users, states, cities, amenities, places, reviews")
        c.execute(query)

    def new(self, obj):
        if not self.__session:
            self.__session = self.Session()
        self.__session.add(obj)

    def save(self):
        if self.__session:
            self.__session.commit()

    def delete(self, obj=None):
        if not self.__session:
            return
        if obj:
            self.__session.delete()
        else:
            self.__session.query(self.__class__).delete()
        self.__session.commit()

    def reload(self):
        # Ensure all tables are created in the database
        Base.metadata.create_all(self.__engine)
        #metadata.create_all()
        self.__session = self.Session()

