#!/usr/bin/python3
""" db storage module """
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage:
    """DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Instanciate the DBStorage class"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dict of __objetc"""
        dic = {}

        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for obj in query:
                k = "{}.{}".format(type(obj).__name__, obj.id)
                dic[k] = obj
        else:
            classes = [State, City, User, Place, Review]
            for clas in classes:
                query = self.__session.query(clas)
                for obj in query:
                    k = "{}.{}".format(type(obj).__name__, obj.id)
                    dic[k] = obj
        return (dic)

    def new(self, obj):
        """Add object in the table"""
        self.__session.add(obj)

    def save(self):
        """Saves all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object in the table"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Configure the session"""
        Base.metadata.create_all(self.__engine)
        Sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Sess)
        self.__session = Session()
