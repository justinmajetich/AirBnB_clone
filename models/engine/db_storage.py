#!/usr/bin/python3

from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv


class DBStorage:
    """  """

    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the connection to the database """

        db_conn = {
            "dialect": "mysql",
            "driver": "mysqldb",
            "host": getenv("HBNB_MYSQL_HOST"),
            "port": 3306,
            "user": getenv("HBNB_MYSQL_USER"),
            "pass": getenv("HBNB_MYSQL_PWD"),
            "db": getenv("HBNB_MYSQL_DB")
        }
        conn_format = '{dialect}+{driver}://{user}:{pass}@{host}:{port}/{db}'

        self.__engine = create_engine(conn_format.format(**db_conn), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session all
            objects depending of the class name.
        """
        all_cls = [State, City, User, Place, Review, Amenity]

        cls_dict = {}
        objs = []

        if cls:
            objs = self.__session.query(cls).all()

        else:
            for cls in all_cls:
                objs += self.__session.query(cls)

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            cls_dict[key] = obj

        return cls_dict

    def new(self, obj):
        """ Add the object to the current database session """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)

        self.__session = Session()

    def close(self):
        """ Close the session """
        self.__session.close()
