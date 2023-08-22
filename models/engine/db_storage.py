#!/usr/bin/python3
"""Defines DBStorage class"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Represents a database storage engine.
    Attributes:
        __engine: SQlAlchemy engine
        __session: SQALchemy session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new instance of DBStorage"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Querys on the current database session all
        objects of the given class
        if cls is None, queries all types of objects
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for eleme in query:
                key = "{}.{}".format(type(eleme).__name__, eleme.id)
                dic[key] = eleme
        else:
            the_list = [State, City, User, Place, Review, Amenity]
            for the_class in the_list:
                query = self.__session.query(the_class)
                for eleme in query:
                    key = "{}.{}".format(type(eleme).__name__, eleme.id)
                    dic[key] = eleme
        return (dic)

    def new(self, obj):
        """Adds a new element in the table"""
        self.__session.add(obj)

    def save(self):
        """saves the changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an element in the table"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Configures"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
