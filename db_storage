#!/usr/bin/python3
"""
New engine DBStorage
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base



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

    def all(self, cls=None)

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
