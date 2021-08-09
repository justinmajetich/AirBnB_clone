#!/usr/bin/python3
"""
    This module defines a class to manage database storage for hbnb clone
"""
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os


class DBStorage:
    """class Data Base storage"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """
            Constructor
        """
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        db = os.environ.get('HBNB_MYSQL_DB')
        host = os.environ.get('HBNB_MYSQL_HOST')
        env = os.environ.get('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user,
                pwd,
                host,
                db
            ),
            pool_pre_ping=True
        )

        if (env == 'test' and db == 'hbnb_test_db'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        list = {}
        if type(cls) == str:
            cls = eval(cls)
        if cls is None:
            for cls in (City, State):
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(type(obj), obj.id)
                    list[key] = obj
        else:
            query = self.__session.query(cls)

            for obj in query.all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                list[key] = obj

        return list

    def new(self, prmObj):
        """Adds new object to storage dictionary"""
        self.__session.add(prmObj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self, prmObj=None):
        """Delete object from storage"""
        if prmObj is not None:
            self.__session.delete(prmObj)

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        sessionFactory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(sessionFactory)
        self.__session = Session()
