#!/usr/bin/python3
"""This module contains the DBStorage class"""
import os
from sqlalchemy import create_engine,  inspect, Column, Integer
from sqlalchemy.orm import sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the DBStorage engine object"""
        url = 'mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("HBNB_MYSQL_USER"), os.getenv(
                "HBNB_MYSQL_PWD"), os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB"))

        DBStorage.__engine = create_engine(url, pool_pre_ping=True)
      #   Drop all tables if in test mode
        if os.getenv("HBNB_ENV") == "test":
            with DBStorage.__engine.connect() as conn:
                for table in DBStorage.__engine.table_names():
                    conn.execute(
                        "DROP TABLE IF EXISTS {}".format(table))

    def all(self, cls=None):
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        objects = {}
        if cls is None:
            # classes = [User, State, City, Amenity, Place, Review]
            classes = [State, City]
            for clas in classes:
                for obj in DBStorage.__session.query(clas):
                    objects["{}.{}".format(clas.__name__, obj.id)] = obj
        else:
            for obj in DBStorage.__session.query(cls):
                objects["{}.{}".format(cls.__name__, obj.id)] = obj
        return objects

    def new(self, obj):
        DBStorage.__session.add(obj)

    def save(self):
        DBStorage.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            DBStorage.__session.delete(obj)

    def reload(self):
        from models.base_model import Base, BaseModel
        from models.city import City
        from models.state import State
        Base.metadata.create_all(DBStorage.__engine)
        DBStorage.__session = sessionmaker(
            bind=DBStorage.__engine, expire_on_commit=False)()
