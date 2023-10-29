#!/usr/bin/python3
"""DB Storage"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        db_config = {
            "dialect": "mysql",
            "driver": "mysqldb",
            "user": os.getenv("HBNB_MYSQL_USER"),
            "password": os.getenv("HBNB_MYSQL_PWD"),
            "host": os.getenv("HBNB_MYSQL_HOST", "localhost"),
            "database": os.getenv("HBNB_MYSQL_DB")
        }

        self.__engine = create_engine(
            f"{db_config['dialect']}+{db_config['driver']}://"
            f"{db_config['user']}:{db_config['password']}@"
            f"{db_config['host']}/{db_config['database']}",
            pool_pre_ping=True
        )

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, clas=None):
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            classes = [cls]

        objects = {}
        for cls in classes:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
