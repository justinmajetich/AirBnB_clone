#!/usr/bin/python3
"""model - dbatabase engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.user import User
from models.base_model import Base

class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        db_path = ('mysql+mysqldb://{}:{}@{}/{}'
                .format(user, passwd, host, db))

        self.__engine = create_engine(db_path, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dictionary = {}
        if cls is None:
            classes = [State, City]
            for class_name in classes:
                for obj in self.__session.query(class_name):
                    key = obj.__class__.__name__ + '.' + obj.id
                    dictionary[key] = obj
        else:
            for obj in self.__session.query(cls):
                key = self.__class__.__name__ + '.' + obj.id
                dictionary[key] = obj
        return dictionary

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()
        finally:
            self.__session.close()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)

        self.__session = session()
