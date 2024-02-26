#!/usr/bin/python3
    """Module that houses the database storage engine
    """

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import environ
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


running_environment = environ["HBNB_ENV"]
user = environ["HBNB_MYSQL_USER"]
pw = environ["HBNB_MYSQL_PWD"]
host = environ["HBNB_MYSQL_HOST"]
db = environ["HBNB_MYSQL_DB"]
connect_script = f"mysql+mysqldb://{user}:{pw}@{host}:3306/{db}"

class DBStorage:
    """Engine responsible for connecting to database and 
    executing SQL queries
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(connect_script, pool_pre_ping=True)
        self.__session = sessionmaker(bind=self.__engine)
        #  Drop all tables if environment is in 'test' mode
        if running_environment == "test":
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
        if cls is None:
            query = self.__session.query(Base).all()
        else:
            query = self.__session.query(cls).all()
        # fill in object dictionary with object IDs as key valeues
        for obj in query:
            obj_dict[f'{obj.__class__.__name__}.{obj.id}'] = obj
        return obj_dict
    
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
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Reloads the database, effectively creating all tables in DB
        """
        Base.metadata.create_all(self.__engine)
        created_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(created_session)

