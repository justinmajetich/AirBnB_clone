#!/usr/bin/python3
"""New storage engine to replace file storage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review


class DBStorage:
    """Storage engine to be used in a MySQL database"""
    __engine: None
    __session: None

    def __init__(self):
        """ Initialize DBStorage """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
                 f"mysql+mysqldb://{user}:{password}@{host}/{database}",
                 pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """queries objects from the database session based on class name"""
        objects = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    jey = f"{obj.__clss__.__name__}.{obj.id}"
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add a new object"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Save to the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
