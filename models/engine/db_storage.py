#!/usr/bin/python3
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.place import Place
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """creates the engine"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}"
            .format(user, password, host, database), pool_pre_ping=True)

    def all(self, cls=None):
        all_classes = ["State", "City", "Amenity", "Place", "Review", "User"]
        object_list = []
        if cls is None:
            for all_classes in object_list:
                object_list.extend(self.__session.query(all_classes))
        else:
            if type(cls) == str:
                cls = eval(cls)
            object_list = self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__,
                               obj.id): obj for obj in object_list}

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        ze_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ze_session)
        self.__session = Session

    def close(self):
        self.__session.close()
