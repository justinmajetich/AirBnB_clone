#!/usr/bin/python3
'''Database engine'''
import mysqldb
import models
from os import getenv
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"User":User, "State": State, "City": City,
           "Amenity": Amenity,"Place": Place, "Review": Review}


class DBFileStorage:
    '''Doc later'''
    __engine = None
    __session = None


    def __init__(self):
        """Initiator"""
        connect = 'mysql+mysqldb://{}:{}@{}/{}'
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(connect.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                        HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.engine)

    def all(self, cls=None):
        """Query all objects from a class (Table)"""

            classes = {"User":User, "State": State, "City": City, "Amenity": Amenity, Place, Review]
            new_row_dict = {}
            for clss in classes:
                if cls is None or cls is clss or cls is in classes[clss]:
                    query = self.__session.query(classes[cls]).all()
                    for obj in query:
                        key = obj.__class__.__name__ + '.' + obj.id
                        new_row_dict[key] = obj
            return (new_dict)


    def new(self, obj):
        """Add new object to db"""
        self.__session.add(obj)


    def save(self):
        """Commit all changes"""
        self.__session.commit()


    def delete(self, obj=None):
        """Delete an object from the db table"""
        if obj:
            self.__session.delete(obj)
            self.save()'''to be reconsidered'''


    def reload(self):

        """Reload all data from db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit=False, scoped_s)
        Session = scoped_session(session_factory)
        self.__session = Session()


    def close(self):
        """A remove() method to remove or terminate the session"""
        self.__session.close()

