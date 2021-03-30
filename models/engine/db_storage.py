#!/usr/bin/python3
"""Module with new DBStorage"""

import os
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage():
    """Class that represents DBStorage"""

    '''** CAN WE EVEN USE SELF HERE WHEN IT WASN'T PASSED IN
    FOR CLASS DBSTORAGE **'''
    __engine = None
    __session = None

    def __init__(self):
        """Method to instantiate class DBStorage attributes"""

        theUser = os.getenv('HBNB_MYSQL_USER')
        thePwd = os.getenv('HBNB_MYSQL_PWD')
        theHost = os.getenv('HBNB_MYSQL_HOST')
        theDB = os.getenv('HBNB_MYSQL_DB')
        theEnv = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(theUser, thePwd,
                                              theHost, theDB),
                                      pool_pre_ping=True)

        '''** add Base to metadata and change
        theEngine to self.__engine **'''
        if theEnv == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to retrieve all objects depending of the class name"""
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.base_model import BaseModel
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity

        classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
        if cls:
            newDict = {}
            allClassObjs = self.__session.query(classes[cls]).all()
            for obj in allClassObjs:
                key = type(obj).__name__ + "." + obj.id
                value = obj.to_dict()
                newDict[key] = value
            return (newDict)
        else:
            allDicts = {}

            dictList = []
            State = self.all('State')
            City = self.all('City')
            dictList.append(State)
            dictList.append(City)

            '''
            User = self.all('User'),
            Amenity = self.all('Amenity'),
            Place = self.all('Place'),
            Review = self.all('Review'))'''

            for dicts in dictList:
                allDicts.update(dicts)

            return(allDicts)

    def new(self, obj):
        """ add the object to current database session"""

        self.__session.add(obj)

    def save(self):
        """Commits all changes of current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Method that deletes from current database session"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloading database with the stuff from the database"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        sessionFactory = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(sessionFactory)
        self.__session = Session()
