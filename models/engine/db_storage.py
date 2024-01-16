#!/usr/bin/python3
"""
New engine DBStorage
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State


class DBStoroge:
    """
    class reprensenting the database storage engine
    """
    __engine = None
    __session = None

    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }


    def __init__(self):
        """Initialize DBStorage instance"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'.
                format(os.getenv('HBNB_MYSQL_USER'),
                    os.getenv('HBNB_MYSQL_PWD'),
                    os.getenv('HBNB_MYSQL_HOST'),
                    os.getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """
        dictionary = {}
        if cls:
            obj = self.__session.query(cls).all()
            for element in obj:
                key = f"{element.__class__.__name__}.{elment.id}"
                dictionary[key] = element
        else:
            for value in self.classes.values():
                obj = self.__session.query(value).all()
                for element in obj:
                    key = f"{element.__class__.__name__}.{element.id}"
                    dictionary[key] = element

        return dictionary

    def new(self, obj):
        """
         add the object to the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()
    
    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj:
            #self.__session.delete(obj)
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """
        Create all tables in the database and create the current
        database session
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()


