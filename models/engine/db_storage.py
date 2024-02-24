#!/usr/bin/python3
"""
New engine DBStorage:
models/engine/db_storage.py
"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, DeclarativeBase
from models.base_model import Base


class DBStorage:
    """
    DBStorage class
    """
    __engine = None
    __session = None

    classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
              }

    def __init__(self):
        """
        __init__ method
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Simulating FileStorage all() method
        """
        result = {}
        theQuery = None
        if cls and not isinstance(cls, str):
            theQuery = self.__session.query(cls).all()
        elif cls and isinstance(cls, str):
            theQuery = self.__session.query(self.classes[cls]).all()
        else:
            theQuery = self.__session.query().all()
        for instance in theQuery:
            key = f'{type(instance).__name__}.{instance.id}'
            result[key] = instance
        return result

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current
        database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_pre = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_pre)
        self.__session = Session

    def close(self):
        """
        call remove() method on the private session attribute
        """
        self.__session.remove()
