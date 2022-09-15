#!/usr/bin/python3

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from os import getenv


class DBStorage:

    classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(f"mysql+mysqldb:\\{HBNB_MYSQL_USER}:\
                                      {HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}\
                                      {HBNB_MYSQL_DB}", pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        temp = {}
        if cls is None:
            for name in self.classes:
                data = self.__session.query(name).all()
                for obj in data:
                    key = obj.__class__.__name__ + '.' + obj.id
                    temp[key] = obj
        else:
            data = self.__session.query(cls).all()
            for obj in data:
                key = obj.__class__.__name__ + '.' + obj.id
                temp[key] = obj
        return temp

    def new(self, obj):
        self.session.add(obj)

    def save(self):
        self.session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.query(obj).delete()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        self.session.close()
