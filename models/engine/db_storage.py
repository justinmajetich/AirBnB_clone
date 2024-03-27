#!/usr/bin/python3
""" New Engine DBStorage """
from sqlalchemy import (create_engine)
from sqlalchemy.schema import MetaData
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """ Return all objects of specific cls or all cls """
        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        classDict = {"City": City, "State": State,
                     "User": User, "Place": Place,
                     "Review": Review, "Amenity": Amenity}
        objects = {}
        if cls is None:
            for className in classDict:
                data = self.__session.query(classDict[className]).all()
                for obj in data:
                    objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

        else:
            if isinstance(cls, str):
                cls = classDict[cls]
            data = self.__session.query(cls).all()
            for obj in data:
                objects[f"{obj.id}"] = obj
        return objects

    def new(self, obj):
        """ Adds the object to the current
        database session (self.__session) """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Reload data from the database """
        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
