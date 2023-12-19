#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import MetaData, inspect
from models.base_model import BaseModel, Base
import os


class DBStorage:
    """Definition of the class"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiation of the class"""
        USER = os.getenv('HBNB_MYSQL_USER')
        PASS = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DB_NAME = os.getenv('HBNB_MYSQL_DB')
        _ENV = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PASS, HOST, DB_NAME), pool_pre_ping=True)

        if _ENV == 'test':
            metadata = MetaData()
            metadata.drop_all(bind=self.__engine)

        # Session = sessionmaker(bind=self.__engine)
        # self.__session = Session()

    def all(self, cls=None):
        """Selection objects, with optional filtering
        by classnames"""
        classes = []
        if cls:
            classes.append(cls)
        else:
            for table_name in Base.metadata.tables:
                mapped_class = None
                for mapper in Base.registry.mappers:
                    if mapper.tables[0].name == table_name:
                        mapped_class = mapper.class_
                        classes.append(mapped_class)
                        break

        dict_s = {}
        for cls in classes:
            all_rows = self.__session.query(cls).all()
            for r in all_rows:
                cls_name = r.__class__.__name__
                dict_s.update({f"{cls_name}.{r.id}": r})
        return dict_s

    def new(self, obj):
        """Adds obj to the session"""
        # if obj:
        self.__session.add(obj)

    def save(self):
        """Saves all changes to the session"""
        # self.__session.add_all()
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database &
        create the current database session"""
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
