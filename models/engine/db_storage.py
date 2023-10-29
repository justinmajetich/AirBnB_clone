#!/usr/bin/python3
"""Class DBStorage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }


class DBStorage:
    """Class for interacting with the database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize instance of DBStorage"""

        # Get environmental variables
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        # start engine
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}'
                                      f'@{host}/{database}', pool_pre_ping=True)

        # check if test
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query current DB for all objects of class (cls)"""
        obDict = {}
        for typeClass in classes.keys():
            if cls == typeClass or cls == classes[typeClass] or cls is None:
                objs = self.__session.query(classes[typeClass]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    obDict[key] = obj
                    if '_sa_instance_state' in obDict:
                        print("Going here")
                        obDict.pop('_sa_instance_state')
        return obDict

    def new(self, obj):
        """Adds a new object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all the data from database into current session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
