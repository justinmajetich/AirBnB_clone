#!/usr/bin/python3
""" database storage engine """

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.base_model import Base

classes = {"City": City, "State": State, "User": User, "Place": Place,
           "Review": Review, "Amenity": Amenity}


class DBStorage:
    """ database storage engine for mysql storage """
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine"""
        port = 3306
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")

        db_uri = "mysql+mysqldb://{}:{}@{}:{}/{}".format(
                user, passwd, host, port, db_name)

        self.__engine = create_engine(db_uri, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ """
        new_dict = {}
        if cls:
            if type(cls) == str:
                cls = classes[cls]

            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + "." + obj.id
                new_dict[key] = obj
        else:
            for clas in classes.values():
                objs = self.__session.query(clas).all()

                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """ adds the obj to the current db session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current db session """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes from the current databse session the obj
            is it's not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reloads database """
        Base.metadata.create_all(self.__engine)
        sesn_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesn_factory)
        self.__session = Session()

    def close(self):
        """ closes working SQLAlchemy session """
        self.__session.close()
