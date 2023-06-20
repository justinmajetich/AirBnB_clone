#!/usr/bin/python3
"""
    db_storage.py
    A script for the class DBStorage
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review


class DBStorage:
    """Database storage engine object"""
    __engine = None
    __session = None

    def __int__(self):
        """create the engine self.__engine and links to MYSQL database"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                            HBNB_MYSQL_USER,
                            HBNB_MYSQL_PWD,
                            HBNB_MYSQL_HOST,
                            HBNB_MYSQL_DB),
                            pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query database depending on class name in arg cls"""
        if cls is None:
            obj_query = self.__seesion.query(State).all()
            obj_query.extend(self.__session.query(City).all())
            obj_query.extend(self.__session.query(User).all())
            obj_query.extend(self.__session.query(Place).all())
            obj_query.extend(self.__session.query(Review).all())
            obj_query.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            obj_query = self.__session.query(cls)
        return {"{}.{}".format(type(i).__name__, i.id): i for i in obj_query}

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        """creat all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session_scoped = scoped_session(session)
        self.__session = Session_scoped()

    def close(self):
        """closese a session"""
        self.__session.close()
