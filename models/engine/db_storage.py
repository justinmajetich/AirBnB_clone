#!/usr/bin/python3
"""This module contains the class DBStorage that serializes instances to a JSON file and deserializes JSON file to instances"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """This class serializes instances to a database and deserializes database to instances"""
    __engine = None
    __session = None

    def __init__(self):
        """This method initializes the SQL database storage engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        DATABASE_URL = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            user, passwd, host, db_name
        )
        self.__engine = create_engine(
            DATABASE_URL, pool_pre_ping=True
        )
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objects = dict()
        all_classes = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_type in all_classes:
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects
    def delete(self, obj=None):
        """Removes an object from storage database"""
        if obj is not None:
            self.__session.query(type(obj)).filter_by(type(obj).id == obj.id).delete(
                synchronize_session=False
            )
    def new(self, obj):
        """Adds an object to the database storage"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e
    
    def save(self):
        """Saves changes to the database"""
        self.__session.commit()
    def reload(self):
        '''Reloads the database'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()
    def close(self):
        '''Closes the session'''
        self.__session.close()