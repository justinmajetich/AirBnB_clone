#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from models.city import Amenity
from models.city import Place
from models.city import Review
from models.city import State
from models.city import User


classes = {"Amenity": Amenity, 
           "City": City, 
           "Place": Place,
           "Review": Review, 
           "State": State, 
           "User": User}
class DBStorage:
    """Database storage"""
    __engine == None
    __session == None

    def __init__(self):
        """Instantiates DBStorage Object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                  format(HBNB_MYSQL_USER,
                                         HBNB_MYSQL_PWD,
                                         HBNB_MYSQL_HOST,
                                         HBNB_MYSQL_DB))

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
        
    #initialize the session
        self.reload()

    def reload(self):
        """reloads data"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def all(self, cls=None):
        """query on the current database session """
        new_dict = {}
        for class_name in classes:
            if cls is None or cls is classes[class_name] or cls is class_name:
                objs = self.__session.querry(classes[class_name]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        """adds object to the database current session"""
        self.__session(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session"""
        if not self.__session:
            self.reload()
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """remove current session if active"""
        self.__session.remove()
