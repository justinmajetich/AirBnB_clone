#!/usr/bin/python3
""" defines the db storage module """

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base

classes = {
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}

class DBStorage:
    """ defines the attributes and methods to be used incase of DBStorage """

    __engine = None
    __sessions = None

    def __init__(self, *args, **kwargs):
        """ initializes the engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'\
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                    os.getenv('HBNB_MYSQL_PWD'), os.getenv('HBNB_MYSQL_HOST'),\
                                    os.getenv('HBNB_MYSQL_DB'), pool_pre_ping=True))

        if os.getenv('HBNB_ENV') == 'test':
            MetaData().drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query all objects of a class, or all objects if no class is given"""
        if cls:
            cls = classes[cls]  # Get the class from the classes dictionary
            objs = self.__sessions.query(cls).all()
        else:
            objs = []
            for cls in classes.values():
                objs.extend(self.__sessions.query(cls).all())
        return {f'{type(obj).__name__}.{obj.id}': obj for obj in objs}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__sessions.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__sessions.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if not None"""
        if obj:
            self.__sessions.delete(obj)

    def reload(self):
        """Create all tables in the database and the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__sessions = Session()
