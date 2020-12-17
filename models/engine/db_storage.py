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
import os
from sqlalchemy.orm import sessionmaker, scoped_session, relationship


class DBStorage():
    """Class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(os.getenv("HBNB_MYSQL_USER"),
                                              os.getenv("HBNB_MYSQL_PWD"),
                                              os.getenv("HBNB_MYSQL_HOST"),
                                              os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metada.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects
        Return a dictionary
        """
        if cls is None:
            ob = self.__session.query(User).all()
            ob.append(self.__session.query(State).all())
            ob.append(self.__session.query(City).all())
            ob.append(self.__session.query(Amenity).all())
            ob.append(self.__session.query(Place).all())
            ob.append(self.__session.query(Review).all())
        else:
            ob = self.__session.query(cls).all()
        new = {}
        for object in ob:
            key = "{}.{}".format(object.__class__.__name__, object.id)
            value = object
            new[key] = value
        return new

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metada.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
