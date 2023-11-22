#!/usr/bin/python3
"""A script that handles database storage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


# environment variables
db_user = getenv("HBNB_MYSQL_USER")
db_passwd = getenv("HBNB_MYSQL_PWD")
db_host = getenv("HBNB_MYSQL_HOST", "localhost")
database = getenv("HBNB_MYSQL_DB")


class DBStorage:
    """A class for manipulating database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """An initialization method to create the instance of DBStorage"""
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(db_user, db_passwd,\
                        db_host, database), pool_pre_ping=True
                )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        """queries objects from database and returns them as dicitionary"""
        if cls is not None:
            dict_obj = {}
            result = self.__session.query(cls).all()
            key = "{}.{}".format(cls.__name__, self.id)
            for obj in result:
                dict_obj[key] = obj
            return dict_obj
        if cls is None:
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            from models.user import User
            classes = [State, City, Amenity, Place, Review, User]
            dict_obj = {}
            for c in classes:
                result = self.__session.query(c).all()
                key = "{}.{}".format(c.__name__, self.id)
                for obj in result:
                    dict_obj[key] = obj
            return dict_obj


    def new(self, obj):
        """Adding an object to the current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates the database schema and session."""
        from models.base_model import Base
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
