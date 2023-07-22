#!/usr/bin/python3
"""
"""

from os import getenv
from sqlalchemy import (create_engine)
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """  """
    __engine = None
    __session = None

    def __init__(self):
        """ create the engine """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST", default="localhost")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """  """
        objDict = {}
        if cls:
            if type(cls) == str:
                cls = eval(cls)

            query = self.__session.query(cls).all()
            for obj in query:
                key = f"{type(obj).__name__}.{obj.id}"
                objDict[key] = obj
        else:
            cls_list = [State, City, User, Place, Review, Amenity]
            for clas in cls_list:
                query = self.__session.query(clas).all()
                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    objDict[key] = obj
        return objDict

    def new(self, obj):
        """ adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ save/commit changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reload """
        Base.metadata.create_all(self.__engine)
        ses_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """ tell our registry to dispose the session """
        self.__session.remove()
        """or self.__session.close()"""
