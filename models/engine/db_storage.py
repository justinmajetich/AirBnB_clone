#!/usr/bin/python3
"""This module defines DBStorage class for database storage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    """This class defines DBStorage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """ Initialise new DBSTorage instance """
        user = getenv("HBNB8MYSQL8USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop.all(self.__engine)

    def all(self, cls=None):
        """Query on current DB session (self.__session)"""
        from models import base_model, user, place, state,
        city, amenity, review

        classes = [base_model.BaseModel, user.User, place.Place,
                   state.State, city.City, amenity.Amenity, review.Review]
        objects = {}
        if cls is not None:
            if isinstance(cls, type) and issubclass(cls, BaseModel):
                cls = cls.__name__
            if cls in classes:
                query_res = self.__session.query(eval(cls)).all()
                for obj in query_res:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        else:
            for c in classes:
                query_res = self.__session.query(c).all()
                for obj in query_res:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Adds object to DB session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Saves changes of current DB session"""
        self.__session.commit()

    def reload(self):
        """Creates all tables in DB"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def delete(self, obj=None):
        """ Deletes from current DB session """
        if obj:
            self.__session.delete(obj)
