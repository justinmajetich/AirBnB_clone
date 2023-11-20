#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    __engine = None
    __session = None

    user = getenv(HBNB_MYSQL_USER)
    pwd = getenv(HBNB_MYSQL_PWD)
    host = getenv(HBNB_MYSQL_HOST)
    db = getenv(HBNB_MYSQL_DB)


    def __init__(self, *args, **kwargs):
        self.__enigne = create_engine('mysql+mysqldb://{}:{}@lcoalhost:{}/{}'.format(user, pwd, host, db), pool_pre_ping=True)
        if (getenv(HBNB_ENV) == 'test'):
            Base.metadata.dropall()
    def all(self, cls=None):
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
                query = self.__session.query(cls)
                for q_object in query:
                    key = "{}.{}".format(type(q_object).__name__, q_object.id)
                    dic[key] = q_object
                else:
                    list_cls = [State, City, User, Place, Review, Amenity]
                    for every_class in list_cls:
                        query = self.__session.query(every_class)
                        for every_obj in query:
                            key = "{}.{}".format(type(every_obj).__name__, every_obj.id)
                            dic[key] = every_obj
                return dic
    def new(self, obj):
        """
        add new obj in current session db
        """
        self.__session.add(obj)

    def save(self):
        """
        commit session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        if obj exist ->  delete obj
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        """
        create the current database session (self.__session) from the engine (self.__engine) by using a sessionmaker
        """
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()

    def close(self):
        """ 
        close session (if needed)
        """
        self.__session.close()

