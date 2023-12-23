#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone
"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage(Base):
    """
    This class manages DB storage for hbnb clone
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Creates the engine self.__engine
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries all objects depending of the class name
        """
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        cls_dict = {"State": State, "City": City, "User": User,
                    "Place": Place, "Review": Review, "Amenity": Amenity}
        objs = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            for c in cls_dict.values():
                objs += self.__session.query(c).all()
        return {type(o).__name__ + "." + o.id: o for o in objs}

    def new(self, obj):
        """
        Adds a new object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and the
        current database session
        """
        Base.metadata.create_all(self.__engine)
        Session1 = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session2 = scoped_session(Session1)
        self.__session = Session2()
