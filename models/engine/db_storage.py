#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        }


class DBStorage(BaseModel):
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """creates new dbstorage instances"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(getenv('HBNB_MYSQL_USER'),
                        getenv('HBNB_MYSQL_PWD'),
                        getenv('HBNB_MYSQL_HOST'),
                        getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """making query sets from the current database instances"""
        my_dict = {}
        queryset = []

        if cls:
            for name, value in classes.items():
                if name == cls:
                    queryset = self.__session.query(value)
                    for objc in queryset:
                        key = name + '.' + objc.id
                        my_dict[key] = objc
            return my_dict
        else:
            for name, value in classes.items():
                queryset = self.__session.query(value)
                for objc in queryset:
                    key = name + "." + objc.id
                    my_dict[key] = objc

        return my_dict

    def new(self, obj):
        """adds new object to database"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.reflesh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """commits chenges of current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes all tables fro database"""
        if obj is not None:
            self.__session.query(type(obj)
                    ).filter(type(obj).id == obj.id).delete()

    def reload(self):
        """creates table in db"""
        Base.metadata.create_all(self.__engine)
        session = (
                sessionmaker(
                    bind=self.__engine, expire_on_commit=False)
                )
        self.__session = scoped_session(session)()

    def close(self):
        """classes class session"""
        self.__session.close()
