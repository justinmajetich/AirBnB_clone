#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import (create_engine)
import os
from sqlalchemy.orm import scoped_session, sessionmaker


hbnb_dev = os.getenv('HBNB_MYSQL_USER')
hbnb_dev_pwd = os.getenv('HBNB_MYSQL_PWD')
localhost = os.getenv('HBNB_MYSQL_HOST')
hbnb_dev_db = os.getenv('HBNB_MYSQL_DB')
hbnb_environ = os.getenv('HBNB_ENV')

class DBStorage():
    """This defines the DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine"""
        from models.base_model import BaseModel, Base
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(hbnb_dev, hbnb_dev_pwd,
                                              localhost, hbnb_dev_db),
                                              pool_pre_ping=True)
        if hbnb_environ == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        new_dict = {}
        if cls != None:
            for instance in self.__session.query(cls).all():
                key = "{}.{}".format(instance.__class__.__name__, instance.id)
                new_dict[key] = instance
            return new_dict
        for instance in self.__session.query(User, State, City,
                                             Amenity, Place, Review).all():
            key = "{}.{}".format(instance.__class__.__name__, instance.id)
            new_dict[key] = instance
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()