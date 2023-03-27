#!/usr/bin/python3
"""Database storage"""


from sqlalchemy.orm import scoped_session
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Database storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates an engine"""

        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """All function"""
        cls_list = ["Reviews", "City", "State", "User",
                    "Place", "Amenity"]
        obj_list = []
        if cls is None:
            for cls_name in cls_list:
                obj_list.extend(self.__session.query(cls_name).all())

        else:
            if type(cls) == str:
                cls = eval(cls)
            obj_list = self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__,
                               obj.id): obj for obj in obj_list}

    def new(self, obj=None):
        """New function"""
        self.__session.add(obj)

    def save(self):
        """Save function"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete function"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload function"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))

    def close(self):
        """Close session"""
        self.__session.close()