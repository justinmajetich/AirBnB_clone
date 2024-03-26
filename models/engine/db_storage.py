#!/usr/bin/python3
"""This class is the storage engine for the database"""
from os import getenv
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base

USER = getenv('HBNB_MYSQL_USER')
PWD = getenv('HBNB_MYSQL_PWD')
HOST = getenv('HBNB_MYSQL_HOST')
DB = getenv('HBNB_MYSQL_DB')

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}


class DBStorage:
    """This class is the storage engine for the database"""
    __engine = None
    __session = None

    def __init__(self):
        """This method creates a new instance of DBStorage"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{USER}:{PWD}@{HOST}/{DB}", pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This method queries the current database session"""
        dictio = {}
        if cls:
            for item in self.__session.query(cls):
                key = f"{item.__class__.__name__}.{item.id}"
                dictio[key] = item
        else:
            for key, value in classes.items():
                for item in self.__session.query(value):
                    key = f"{item.__class__.__name__}.{item.id}"
                    dictio[key] = item
        return dictio

    def new(self, obj):
        """This method adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """This method commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """This method deletes from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """This method creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
