#!/usr/bin/python3

import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
import MySQLdb

class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        USER = os.getenv('HBNB_MYSQL_USER')
        PASSWORD = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DATABASE = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(USER, PASSWORD, HOST, DATABASE
                                            ), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        classes_dict = {'Amenity': Amenity, 'Place': Place,
                        'User': User, 'Review': Review, 'City': City,
                        'State': State}
        obj = []
        if cls is None:
            for key in classes_dict.keys():
                obj.extend(self.__session.query(classes_dict[key]).all())
        else:
            if type(cls) == str:
                cls = classes_dict[cls]
            obj = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o,id): o for o in obj}


    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()