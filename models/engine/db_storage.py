#!/usr/bin/python3
"""DBStorage engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """DBStorage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects in a dict"""
        if cls is not None:
            cls = eval(cls)
            objects = self.__session.query(User).all()
        else:
            objects = self.__session.query(User).all()
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(State).all())
            objects.extend(self.__session.query(Amenity).all())

        obj_dict = {}
        for obj in objects:
            obj_dict[f"{type(obj).__name__,}.{obj.id}"] = obj

        return obj_dict

    def new(self, obj):
        """add new object to the current database session"""
        self.__session.add(obj)

    def save(self, obj):
        """save new object to the current databse session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine,
                         expire_on_commit=False)
        self.__session = scoped_session(s)
