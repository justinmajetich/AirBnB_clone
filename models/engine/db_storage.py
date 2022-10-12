#!/usr/bin/python3
'''Definition of engine for db storage
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.base_model import Base
from models.amenity import Amenity
import os


class DBStorage():
    '''Class definition for database storage
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''Initializes and establishes all connections for db storage
        '''
        dev_mode = user = password = host = db = ""
        try:
            user = os.getenv('HBNB_MYSQL_USER')
            password = os.getenv('HBNB_MYSQL_PWD')
            host = os.getenv('HBNB_MYSQL_HOST')
            db = os.getenv('HBNB_MYSQL_DB')
            dev_mode = os.getenv('HBNB_ENV')
        except KeyError:
            print("Warning: Some environment variables were not found")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}",
            pool_pre_ping=True)
        if dev_mode and dev_mode.strip() == 'test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        '''Return all the all instances of type cls
        '''
        models = [City, State, User, Place, Review]
        result_dict = {}
        if cls is not None and cls in models:
            for obj in self.__session.query(cls).all():
                result_dict.update(
                    {f"{obj.__class__.__name__}.{obj.id}": obj}
                )
        else:
            for model in models:
                for obj in self.__session.query(model).all():
                    result_dict.update(
                        {f"{obj.__class__.__name__}.{obj.id}": obj}
                    )
        return result_dict

    def new(self, obj):
        '''Adds obj to the current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''Commits all pending changes to the database
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''Delete from the current database session
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''Creates all tables in the database and initializes new session
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
