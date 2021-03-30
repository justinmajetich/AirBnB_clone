#!/usr/bin/python3
"""Module with new DBStorage"""
import os
from sqlalchemy import create engine
from sqlalchemy.schema import MetaData
from sqlalchemy import sessionmaker

class DBStorage:
"""Class that represents DBStorage"""
    self.__engine = None
    self.__session= None

    def __init__(self):
        """Method to instantiate class DBStorage attributes"""
        
        theUser = os.getenv(HBNB_MYSQL_USER)
        thePwd = os.getenv(HBNB_MYSQL_PWD)
        theHost = os.getenv(HBNB_MYSQL_HOST)
        theDB = os.getenv(HBNB_MYSQL_DB)

        self.__engine = theEngine(vroom = 'mysql+mysqldb://{}:{}@localhost/{}'\
            .format(theUser, thePwd, theHost), pool_pre_ping=True)

        if os.getenv(HBNB_ENV) == "test":
            MetaData.drop_all(theEngine)

    def all(self, cls=None):
        """Method to retrieve all objects depending of the class name"""

        if cls:
            newDict = {}
            allClassObjs = self.__session.query(cls).all()
            for obj in allClassObjs:
                key = obj.__name__ + "." + obj.id
                value = obj.__dict__
                newDict[key] = value
            self.__session.close()
            return (newDict)
        else:
            allDicts = {}
            
            dictList = [
            User = self.all(User),
            State = self.all(State),
            City = self.all(City),
            Amenity = self.all(Amenity),
            Place = self.all(Place),
            Review = self.all(Review),
            ]
            
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
        
        Base.metadata.create_all(self.__engine)
        
        sessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessionFactory)
        self.__session = Session()