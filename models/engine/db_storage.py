#!/usr/bin/python3
""" New file storage"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ new sql file storage system """
    __engine = None
    __session = None

    def __init__(self):
        """Set up engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                        .format(getenv("HBNB_MYSQL_USER"),
                                getenv("HBNB_MYSQL_PWD"),
                                getenv("HBNB_MYSQL_HOST"),
                                getenv("HBNB_MYSQL_DB")),
                                pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all method for Db storage class"""
        if cls:
            objs = self.__session.query(eval(cls))
        else:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
        return {"{}.{}".format(type(x).__name__, x.id): x for x in objs}

    def new(self, obj):
        """add object to current __session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reaload all for session"""
        from sqlalchemy.orm import scoped_session
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine,
                expire_on_commit=False)
        Session = scoped_session(sesh)
        self.__session = Session()
