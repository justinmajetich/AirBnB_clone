#!/usr/bin/python3
""" Class for database storage """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity



class DBStorage:
    """ class attributes """
    __engine = None
    __session = None
    def __init__(self) -> None:
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
        """ Queries and returns all types of objects in the dict """
        dict = {}
        if cls:
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dict[key] = obj
        else:
            list = [State, City, User, Place, Review, Amenity]
            for name in list:
                query = self.__session.query(name)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    dict[key] = obj
        return(dict)
    def new(self, obj):
        """ adds the object to the current database session """
        self.__session.add(obj)
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit(obj)
    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.save()
        else:
            self.__session.delete(obj)
    def reload(self):
        """reload and create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        secur = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(secur)
        self.__session = Session()
    
    


