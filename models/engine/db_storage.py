#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """[summary]
        """        
        enviroment = os.getenv('HBNB_ENV')
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, password, host, database), pool_pre_ping=True)
        
        Session = sessionmaker()
        self.__session = Session()


        if enviroment == "test":
            Base.metadata.drop_all(engine, checkfirst=True)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = self.__session.query(User, State, City, Amenity, Place, Review).all()

        new_dic = {}
        for key in objects.keys():
            key = "{}.{}".format(i.__class__.__name__, i.__dict__.id)
            # Pendienteeee value
            setattr(new_dic, key, objects[key])
        return new_dic



    def new(self, obj):
        """[New object to session]""" 
        self.__session.add(obj)

    def save(self):
        """[Save new changes in databases]"""
        self.__session.commit()

    def delete(self, obj=None):
        """[Delete objects of databases]"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """[Reload objects in databases]"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)            

