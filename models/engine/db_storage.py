#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    """Manages the storage of the content of the console into database """
    __engine = None
    __session = None

    def __init__(self):
        """Initialises the DBStorage Class"""
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        lhost = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        p_env = os.getenv("HBNB_ENV")

        engine_string = "mysql+mysqldb://{}:{}@{}/{}".format(user,passwd,
                                                          lhost, db_name)
        self.__engine = create_engine(engine_string, pool_pre_ping=True)

        if (p_env == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns object dictionary of the data in database """
        obj_dict = {}
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            all_items = self.__session.query(cls).all()
            for items in all_items:
                key_format = items.__class__.__name__ + "." + items.id
                obj_dict[key_format] = items
            return obj_dict
        else:
            classes = {
                'User': User, 'Place': Place, 'State': State,
                'City': City, 'Amenity': Amenity, 'Review': Review
            }
            for value in classes.values():
                all_item = self.__session.query(value).all()
                for item in all_item:
                    key_format = item.__class__.__name__ + "."+ item.id
                    obj_dict[key_format] = item
            return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads up content from the db """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
