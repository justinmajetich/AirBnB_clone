#!/usr/bin/python3
"""db storage module"""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ creates a db storage engine"""
    __engine = None
    __session = None
    classes = ["State", "City", "User", "Place", "Review", "Amenity"]

    def __init__(self):
        """ create engine"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        obj_dict = {}

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)

            if cls.__name__ in DBStorage.classes:
                query = self.__session.query(cls).all()
                
                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    obj_dict.update({key: obj})
        else:
            for cls_ in DBStorage.classes:
                query = self.__session.query(eval(cls_)).all()

                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    obj_dict.update({key: obj})

        return obj_dict

    def new(self, obj):
        if type(obj).__name__ in DBStorage.classes:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj and type(obj).__name__ in DBStorage.classes:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ calls close()
        """
        self.__session.close()
