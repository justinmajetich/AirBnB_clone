#!/usr/bin/python3
"""DBStorage Engine"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
import json
from sqlalchemy.orm import sessionmaker, scoped_session

clas = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage():
    """Class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metada.drop_all(self.__engine)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sessionM = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessionM)
        self.__session = Session()
    
    def all(self, cls=None):
        """query on the current database session all objects
        Return a dictionary
        """
        new_dict = {}
        for clss in clas:
            if cls is None or cls is clas[clss] or cls is clss:
                objs = self.__session.query(clas[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
