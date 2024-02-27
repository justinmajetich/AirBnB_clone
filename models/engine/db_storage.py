#!/usr/bin/python3
"""Module that houses the database storage engine
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

usr = getenv('HBNB_MYSQL_USER')
pw = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
connect_script = 'mysql+mysqldb://{}:{}@{}:3306/{}'


class DBStorage:
    """Engine responsible for connecting to database and
    executing SQL queries
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(connect_script.format
                                      (usr, pw, host, db), pool_pre_ping=True)
        #  Drop all tables if environment is in 'test' mode
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method that returns dictionary list of all objects of certain class
        If no class specified, queries all types of objects

        Args:
            cls : Class of object (defauilts to None)

        Returns:
            obj_dict : A dictionary containing objects of a certain class
            Format :
        """
        obj_dict = {}
        if cls:
            if isinstance(cls, str):
                cls = getattr(models, cls, None)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                obj_dict[key] = elem
        else:
            attr_list = [State, Amenity, Review, Place, City, User]
            for clss in attr_list:
                query = self.__session.query(clss)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    obj_dict[key] = elem
        return (obj_dict)

    def new(self, obj):
        """Add the object to the current database session
        allowing it to be committed to the database

        Args:
            obj : the object to be added to DB session
        """
        self.__session.add(obj)

    def save(self):
        """Commit changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deleted specified object from current database session

        Args:
            obj : The object to be deleted from session. Defaults to None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the database, effectively creating all tables in DB
        """
        Base.metadata.create_all(self.__engine)
        created_session = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(created_session)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
