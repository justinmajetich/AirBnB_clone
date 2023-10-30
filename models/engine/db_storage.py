#!/usr/bin/python3
"""DB Storage"""
import os
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class DBStorage:
    """MySQL database interaction"""
    __engine = None
    __session = None


def __init__(self):
    self.__engine = create_engine(
        "mysql+mysqldb://{user}:{pwd}@{host}/{db}".format(
            user=os.getenv('HBNB_MYSQL_USER'),
            pwd=os.getenv('HBNB_MYSQL_PWD'),
            host=os.getenv('HBNB_MYSQL_HOST'),
            db=os.getenv('HBNB_MYSQL_DB')
        ),
        pool_pre_ping=True
    )

    if os.getenv('HBNB_ENV') == "test":
        Base.metadata.drop_all(self.__engine)

    session_factory = sessionmaker(
        bind=self.__engine, expire_on_commit=False
    )
    Session = scoped_session(session_factory)
    self.__session = Session

    def all(self, clas=None):
        """Query on current DB"""
        new_dict = {}
        for cls_name, cls in classes.items:
            if cls is None or cls is classes[cls_name] or cls is cls_name:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """adding obj to db sesh"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to db sesh"""
        self.__session.commit()

    def delete(self, obj=None):
        """deleting from current db sesh obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session
