#!/usr/bin/env python3

import os

from typing import Any, Union
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import DatabaseError
from models.base_model import BaseModel, Base
from models.city import *
from models.state import *

Entity = Union[Base, BaseModel]


class DataSource:
    __engine = None
    __session = None
    __connection_url = ''
    __port = int(os.getenv('HBNB_DB_PORT', 3306))
    __user = os.getenv('HBNB_MYSQL_USER')
    __password = os.getenv('HBNB_MYSQL_PWD')
    __host = os.getenv('HBNB_MYSQL_HOST')
    __database = os.getenv('HBNB_MYSQL_DB')
    __dialect = 'mysql'
    __driver = 'mysqldb'

    def __init__(self) -> None:
        self.__connection_url = f"{self.__dialect}+{self.__driver}://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}"
        self.__engine = create_engine(
            self.__connection_url, pool_pre_ping=True)
        if self.engine is not None:
            Base.metadata.create_all(self.__engine)
        Session = sessionmaker()
        Session.configure(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    @property
    def engine(self):
        return self.__engine

    @property
    def session(self):
        return self.__session

    def get_connection_details(self):
        return self.__connection_url


class DBStorage:
    __engine = None
    __session = None

    entity_map: dict[str, Entity] = {
        'State': State, 'City': City
    }

    def __init__(self) -> None:
        self.datasource = DataSource()
        self.__engine = self.datasource.engine
        self.__session = self.datasource.session

    @property
    def engine(self):
        return self.__engine

    @property
    def session(self):
        return self.__session

    def new(self, entity, **kwargs):
        _class = self.entity_map.get(entity)
        if not _class:
            print("** class doesn't exist **")
            return None
        
        instance = _class(**kwargs)
        try:
            if instance is not None:
                self.session.add(instance)
                return instance.id
        except DatabaseError:
            self.session.rollback()
            return None
        else:
            self.session.commit()
            return instance.id


    def reload(self):
        pass

    def all(self, entity):
        _class = self.entity_map.get(entity)
        if not _class:
            print("** class doesn't exist **")
            return None
        
        return self.session.query(_class).order_by(_class.id).all()
        
