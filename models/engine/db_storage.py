#!/usr/bin/python3
from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():

    __engine = None
    __session = None

    def __init__(self):

        user = getenv(HBNB_MYSQL_USER)
        password = getenv(HBNB_MYSQL_PWD)
        host = getenv(HBNB_MYSQL_HOST)
        database = getenv(HBNB_MYSQL_DB)
        tmp = getenv(HBNB_ENV)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
        (user, password, host, database), pool_pre_ping=True)

        if tmp is 'test':
            Base.metadata.drop_all(self.__engine)
            # If fails remember to review this part

    def all(self, cls=None):

        classes = {
               'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

        dictionary = {}

        if cls == None:
            for key, value in classes:
                objetos = self.__session.query(value).all()
                for obj in objetos:
                    dictionary[obj.__name__ + obj.__dict__['id']] = obj 
        elif cls:
            # comment to review
            objetos = self.__session.query(cls).all()
            for obj in objetos:
                dictionary[obj.__name__ + obj.__dict__['id']] = obj

        return(dictionary)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
