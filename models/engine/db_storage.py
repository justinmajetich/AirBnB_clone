#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from os import getenv


class DBStorage(FileStorage):
    """ Class for DBStorage """
    __engine = None
    __session = None
    _FileStorage__objects = {}

    def __init__(self):
        """"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        self.reload()

    def all(self, cls=None):
        """Database sessions"""
        objects = {}
        classes = [State, City, User, Amenity, Place, Review]

        if cls is None:
            for class_name in classes:
                objects.update({f"{obj.__class__.__name__}.{obj.id}": obj
                                for obj in self.__session.query(class_name)
                                .all()})

        else:
            if cls in classes:
                for obj in self.__session.query(cls).all():
                    objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

        return objects

    def new(self, obj):
        """ Adds object """
        return self.__session.add(obj)

    def save(self):
        """ Saves to database """
        return self.__session.commit()

    def delete(self, obj=None):
        """ Deletes object """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates session """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
