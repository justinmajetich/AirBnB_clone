#!/usr/bin/python3
""" class to manage databse """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
    'BaseModel': BaseModel, 'User': User,  'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review}


class DBStorage:
    """ Represent database storage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ initialize the database """
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query current database """
        obj_dict = {}
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                obj_key = obj.__class__.__name__ + '.' + obj.id
                obj_dict[obj_key] = obj
        return obj_dict

    def new(self, obj):
        """ add obj to current database session """
        self.__session.add(obj)

    def save(self):
        """ commit changes to current database """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete obj from database if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
