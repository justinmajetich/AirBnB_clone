#!/usr/bin/python3
"""New engine DBStorage"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Class that manages DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on database session"""
        query_obj = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = f'{obj.__class__.__name__}.{obj.id}'
                query_obj[key] = obj
        else:
            classes = [state.State, city.City, user.User]
            for cls in classes:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    query_obj[key] = obj
        return query_obj
    
    def new(self, obj):
        """New objects"""
        self.__session.add(obj)

    def save(self):
        """Commits changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deeltes an object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads Object"""
        Base.metdata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()