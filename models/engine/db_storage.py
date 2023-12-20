#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


HBNB_MYSQL_USER = getenv("USER")
HBNB_MYSQL_PWD = getenv("PASSWORD")
HBNB_MYSQL_HOST = getenv("HOSTNAME")
HBNB_MYSQL_DB = getenv("DATABASE")
HBNB_ENV = getenv("ENVIRONMENT")
DIALECT = "mysql"
DRIVER = "mysqldb"
CLASSES = [User, Place, State, City, Amenity, Review]


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiates a  new model
        Attributes:
            self.__engine (object) : SQLAlchemy Instance connection engine
        """
        self.__engine = create_engine(
            "{}+{}://{}:{}@{}/{}".format(DRIVER, DIALECT, HBNB_MYSQL_USER,
                                         HBNB_MYSQL_PWD, HBNB_MYSQL_HOST,
                                         HBNB_MYSQL_DB), pool_pre_ping=True
        )
        # Drop all tables if HBNB_ENV equals 'test'
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries the database for all objects depending on the class name
        Arguments:
            cls (Object): Class (Table) to view
        Return:
            obj_dict (dict): Dictionary containing the class name, id & object
        """
        obj_dict = {}
        if cls in CLASSES:
            dict_key = "{}.{}".format(cls.__class__.__name__, cls.id)
            obj_dict[dict_key] = self.__session.query(cls).all()
        else:
            for clss in CLASSES:
                dict_key = "{}.{}".format(clss.__class__.__name__, clss.id)
                obj_dict[dict_key] = self.__session.query(clss).all()

        return obj_dict

    def new(self, obj):
        """ Adds the object to the current database session
        Attribute:
            obj (obj) : A Class instance from one of the Tables
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not none
        Attributes:
            obj (obj): A class instance from one of the Tables
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database and creates the current data
        session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
