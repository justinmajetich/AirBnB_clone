#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import engine

user = os.getenv('HBNB_MYSQL_USER')
pw = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')

classes = {
    'City': City,
    'User': User,
    'Review': Review,
    'State': State,
    'Place': Place,
    'Amenity': Amenity
    }

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ the init that give HBNB envelopes?"""

        dir = "mysql+mysqldb://{}:{}@{}/{}" \
            .format(user, pw, host, db)

        self.__engine = create_engine(dir, pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        class_dict = {}
        if not cls:
            for actual_class in classes.values():
                object_list = self.__session.query(actual_class).all()
                for obj in object_list:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    class_dict[key] = obj
        else:
            object_list = self.__session.query(cls).all()
            for obj in object_list:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                class_dict[key] = obj
        return class_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ method reload creates a session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
