#!/usr/bin/python3
"""DBStorage uses SQLAlchemy, and connects with database"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import classes
import models


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes database connection"""
        user_name = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user_name, pwd, host, db), pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Retrieves dict of all objects in database"""
        objs_dict = {}
        objs = None
        if cls:
            if type(cls) is str and cls in classes:
                cls = classes[cls]
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(User, State, City, Place).all()
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objs_dict[key] = obj
        return (objs_dict)

    def new(self, obj):
        """Makes query depending on class name"""
        self.__session.add(obj)

    def save(self):
        """Save all changes with commit"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object if any"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Reloads session in db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close session"""
        self.__session.close()
