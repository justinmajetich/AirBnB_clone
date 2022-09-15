#!/usr/bin/python3
"""This module defines a class to manage database storage for AirBnB clone"""
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


all_models = {'User': User, 'Place': Place,
              'State': State, 'City': City, 'Amenity': Amenity,
              'Review': Review
              }


class DBStorage:
    """This class manages storage of airbnb models in the database"""
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize new instance """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=State):
        """Returns models currently in the database"""
        filtered_dict = {}
        print(self.__session.query(all_models[cls.__name__]).all())
        print("Entered here\n")
        for model in all_models:
            if cls == all_models[model]:
                print(self.__session.query(all_models[cls.__name__]).all())
                print(cls.__name__)
                """instances = self.__session.query(all_models[model]).all()
                for instance in instances:
                    filtered_dict[instance] = instance
                    print("Here works")"""
        return filtered_dict

    def new(self, obj):
        """Adds new object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commit """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes object if obj is passed, else do nothing"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
