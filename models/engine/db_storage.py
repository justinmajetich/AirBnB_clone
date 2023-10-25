#!/usr/bin/python3
"""class to manage database storage"""

import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base


class DBStorage:
    """manage database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor for DBStorage class"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """queries all objects depending on the clas name"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        objects = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls is None:
            classes = [cls for cls in classes if cls is not None]
        else:
            classes = [cls]

        for cls in classes:
            query = self.__session.query(cls)
            for item in query:
                key = '{}.{}'.format(type(item).__name__, item.id)
                objects[key] = item

        return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and current database session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ Closes the current session """
        self.__session.remove()
