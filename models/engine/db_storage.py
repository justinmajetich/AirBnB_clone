#!/usr/bin/python3
"""
This module defines a DB storage engine for hbnbclone
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Manaages storage of hbnb models in MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initiliazes the SQL database storage"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        DB_URL = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            user, pwd, host, db
            )
        self.__engine = create_engine(
            DB_URL, pool_pre_ping=True
            )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries a dictionary of models in storage
        """
        obj_dict = {}
        classes = [User, State, City, Amenity, Place, Review]
        if cls is None:
            for cl in classes:
                obj_dict.update({obj.id: obj for obj in self.__session.query(cl).all()})
        else:
            for obj in self.__session.query(cls).all():
                obj_dict[obj.id] = obj
        return obj_dict

    def new(self, obj):
        """
        Adds new object to storage
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit changes to current db session
        """
        self.__session.commit()

    def reload(self):
        """
        Loads storage database'
        """
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
            )
        self.__session = scoped_session(SessionFactory)()