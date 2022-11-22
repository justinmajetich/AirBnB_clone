#!/usr/bin/python3
"""New Engine DBStorage"""
import os
from models.base_model import BaseModel
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import MetaData


class DBStorage:
    """class of database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize the new engine creation"""
        engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                               .format(getenv("HBNB_MYSQL_USER"),
                                       getenv("HBNB_MYSQL_PWD"),
                                       getenv("HBNB_MYSQL_HOST"),
                                       getenv("HBNB_MYSQL_DB")),
                               pool_pre_ping=True)
        if getenv("HBNB_ENV") ==  "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Turns to query the current database session"""
        if cls=None:
            elem = self.__session.query(State).all()
            elem.extend(self.__session.query(City).all())
            elem.extend(self.__session.query(User).all())
            elem.extend(self.__session.query(Place).all())
            elem.extend(self.__session.query(Review).all())
            elem.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            elem = self.__session.query(cls)
        for el in elem:
            cl = "{}.{}".format(type(el).__name__, el.id)
            dict1[cl] = el
            return dict1

    def new(self, obj):
        """adds the objecgt to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """clossing session"""
        self.__session.close()
