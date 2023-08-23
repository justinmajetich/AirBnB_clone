#!/usr/bin/python3
"""
New DataBase Storage Engine
"""

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
models_objs = {
        "User": User,
        "City": City,
        "State": State,
        "Place": Place,
        "Review": Review,
        "Amenity": Amenity
        }


class DBStorage():
    """
    DB engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialization
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session
        """
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                obj_dict[key] = obj
        else:
            for mdl in models_objs.values():
                objs = self.__session.query(mdl).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    obj_dict[key] = obj

        return obj_dict


    def new(self, obj):
        """
        adds the obj to the current database session
        """
        if obj:
            self.__session.add(obj)
            self.save()

    def save(self):
        """
        commit all changes of the current database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delets from the current database
        session of obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Recreate all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

