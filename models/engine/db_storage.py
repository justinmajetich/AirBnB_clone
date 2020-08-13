#!/usr/bin/python3
"""
comments
"""
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """comments"""

    __engine = None
    __session = None

    def __init__(self):
        """comments"""

        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        HB_ENV = getenv('HBNB_ENV')
        STORAGE = getenv('HBNB_TYPE_STORAGE')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(USER, PWD, HOST, DB),
                                      pool_pre_ping=True)

        if HB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session
        all objects depending of the class name
        """
        new_dict = {}
        if cls:
            query = self.__session.query(eval(cls))
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        else:
            classes_list = [User, State, City, Amenity, Place, Review]
            for classes in classes_list:
                query = self.__session.query(classes)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """
        add object to the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        commit all changes of the session
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        """

        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)

        self.__session = session()

    def close(self):
        """
        Close session
        """
        self.__session.close()
