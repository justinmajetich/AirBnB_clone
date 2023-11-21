#!/usr/bin/python3
"""DBStorage module for HBNB project"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


class DBStorage:
    """DBStorage"""
    __engine=None
    __session=None

    def __init__(self):
        """Constructor of class object"""
        DBStorage.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(DBStorage.__engine)

    def all(self, cls=None):
        """All method call"""
        obj = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = DBStorage.__session.query(cls)
            for i in query:
                key = "{}.{}".format(
                        type(i).__name__, i.id)
                obj[key] = i
        else:
            class_name = [
                    State,
                    City,
                    User,
                    Place,
                    Review,
                    Amenity]
            for item in class_name:
                query = DBStorage.__session.query(item)
                for i in query:
                    key = "{}.{}".format(
                            type(i).__name__, i.id)
                    obj[key] = i
        return (obj)

    def new(self, obj):
        """New method call"""
        DBStorage.__session.add(obj)

    def save(self):
        """Save method call"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """Delete method call"""
        if obj:
            DBStorage.__session.delete(obj)

    def reload(self):
        """relaod method call"""
        session_factory = sessionmaker(
                bind=DBStorage.__engine,
                expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        DBStorage.__session = scoped_session(session_factory)

    def close(self):
        """close method call"""
        self.__session.close()
