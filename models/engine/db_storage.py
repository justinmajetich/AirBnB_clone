#!/usr/bin/python3
""" Engine for the MySQL database """

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base, BaseModel


class DBStorage:
    """
        Class Instance for MySQL database
        @args:
            Class Instance:
                - __engine = variable to hold the engine of the database
                - __session = variable to hold the session of the database
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Method to initiate the MySQL database """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'), os.getenv('HBNB_MYSQL_DB')
                ), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Method for list or querying objects in the current dataset """
        new_dict={}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            new_query = self.__session.query(cls).all()
            if new_query:
                for news in new_query:
                    class_name = "{}.{}".format(type(news).__name__, news.id)
                    new_dict[class_name] = news.__str__()
            return new_dict
        for Variable in [State, City]:
            all_query = self.__session.query(Variable).all()
            if all_query:
                for keys in all_query:
                    all_name = "{}.{}".format(type(keys).__name__, keys.id)
                    new_dict[all_name] = keys
        return new_dict

    def new(self, obj):
        """ Method to add object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Method to commit all changes to the current database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Method to delete from the current database """
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """ Method to create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
