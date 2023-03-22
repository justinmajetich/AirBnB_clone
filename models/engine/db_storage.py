#!/usr/bin/python3
"""New engine DbStorage"""

import os
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


Class_name = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """Manage DB storage"""

    __engine = None
    __session = None

    def __init__(self):
        # call value in env
        user = os.getenv("HBNB_MYSQL_USER")
        pswd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_MYSQL_ENV")
        # create engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user,
                                              pswd,
                                              host,
                                              db_name),
                                      pool_pre_ping=True
                                      )
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ query on the current database session"""

        #dict_objects = {}
        # OLD VERSION
        # if cls != None:
        #     for obj in self.__session.query(cls).all():
        #         dict_objects.update({'{}.{}'.
        # format(type(cls).__name__, obj.id,): obj})
        # else:
        #     for k, v in Class_name.items():
        #         for obj in self.__session.query(v):
        #             dict_objects.update({'{}.{}'.
        # format(type(obj).__name__, obj.id,): obj})
        # return (dict_objects)

        #if cls is None:
            # call all cls name
            #all_obj = self.__session.query(
                #Amenity, City, Place, Review, State, User).all()
        #else:
            #all_obj = self.__session.query(cls).all()

        # add all_obj in dict
        #for obj in all_obj:
            #dict_objects[obj.__class__.__name__ + '.' + obj.id] = obj

        #return (dict_objects)

        #test3

        classes = [State, City, User, Place, Review, Amenity]
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            all_obj = self.__session.query(cls).all()
        else:
            all_obj = []
            for model_class in model_classes:
                all_obj += self.__session.query(model_class).all()
        result_dict = {}
        for obj in all_obj:
            key = f"{type(obj).__name__}.{obj.id}"
            result_dict[key] = obj
        return result_dict

    def new(self, obj):
        """ add new object to the db session"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """ save all change by commit in the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete object from current db session"""
        if obj is not None:
            self.__session.delete(obj)
        self.save()

    def reload(self):
        """ create db table & session"""
        # create all table
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(session)()

    def close(self):
        """ close db"""
        self.__session.close()
