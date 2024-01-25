#!/usr/bin/python3
""" This module represents the Database engine """
from lib2to3.fixes import fix_itertools_imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ


from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

user = environ.get("HBNB_MYSQL_USER")
pwd = environ.get("HBNB_MYSQL_PWD")
host = environ.get("HBNB_MYSQL_HOST")
env = environ.get("HBNB_ENV")
db = environ.get("HBNB_MYSQL_DB")

Base = declarative_base()


class DBStorage:
    """ Database Storage Class """
    __engine = None
    __session= None

    def __init__(self):
        """ Instantiates new object """
        self.__engine = create_engine(f"mysql+mysqldb://{user}\
        :{pwd}@{host}/{db}", pool_pre_ping=True)
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Makes a query on the current database session """
        new_dict = {}
        if cls:
            result = self.__session.query(cls).all()
            for instance in result:
                key = f"{type(instance).__name__}.{instance.id}"
                new_dict[key] = instance
        else:
            all_classes = [State, City, User, Place, Review, Amenity]
            for clas in all_classes:
                result = self.__session.query(clas)
                for instance in result:
                    key = f"{type(instance).__name__}.{instance.id}"
                    new_dict[key] = instance
        return new_dict

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)
    
    def save(self):
        """ Commit all changes to the current database session """
        if self.__session:
            self.__session.commit()
    
    def delete(self, obj=None):
        """ Delete from the current database session 'obj' if not None """
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """ Create all tables in the database """

        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(expire_on_commit=False)
        self.__session = Session(bind=self.__engine)
