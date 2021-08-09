#!/usr/bin/python3
'''
    Declaration for database storage
'''
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session, exc
import os


class DBStorage():
    '''
    Database storage class
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        Creates engine connection
        '''
        username = os.getenv('HBNB_MYSQL_USER', default=None)
        password = os.getenv('HBNB_MYSQL_PWD', default=None)
        localhost = os.getenv('HBNB_MYSQL_HOST', default=None)
        db_name = os.getenv('HBNB_MYSQL_DB', default=None)
        connection = 'mysql+mysqldb://{}:{}@localhost/{}'
        self.__engine = create_engine(connection.format(
            username, password, db_name), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        Queries current database session based on class.
        Returns a dictionary representation of the query.
        '''
        result = []
        new_dict = {}
        if cls is not None:
            result = self.__session.query(eval(cls)).all()
            for item in result:
                key = item.__class__.__name__ + '.' + item.id
                new_dict[key] = item
        else:
            classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
            for class_name in classes:
                try:
                    result = (self.__session.query(eval(class_name)).all())
                    for item in result:
                        key = item.__class__.__name__ + '.' + item.id
                        new_dict[key] = item
                except Exception:
                    continue
        return new_dict

    def new(self, obj):
        '''
        Adds the object to the current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
        Commits all changes of the current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Deletes from the current database session obj if not None
        '''
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        '''
        Creates all tables in the database.
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        ''' closes a session'''
        self.__session.close()
