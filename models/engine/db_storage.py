#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
import os


class DBStorage:
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(os.environ.get('HBNB_MYSQL_USER'),
                        os.environ.get('HBNB_MYSQL_PWD'),
                        os.environ.get('HBNB_MYSQL_HOST', 'localhost'),
                        os.environ.get('HBNB_MYSQL_DB')),
                pool_pre_ping=True
        )
        if os.environ.get('HBNB_ENV') == 'test':
            self.__engine.drop_all()

    def all(self, cls=None):
        from models import base_model

        session = self.__session
        objects = {}

        if cls is None:
            classes = [base_model.State,
                       base_model.City,
                       base_model.User,
                       base_model.Amenity,
                       base_model.Place,
                       base_model.Review]
            for cs in classes:
                objects.update({obj.id: obj for obj in session.query(cl).all()})
        else:
            objects.update({obj.id: obj for obj in session.query(cls).all()})

        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
