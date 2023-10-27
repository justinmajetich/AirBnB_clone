#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Creates a database with SQLAchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializies the engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB"),
                                              pool_pre_ping=True))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        r_dict = {}

        if cls:
            result = self.__session.query(cls).all()
            for ob in result:
                key = "{}.{}".format(type(ob).__name__, ob.id)
                r_dict[key] = ob
        else:
            for m_class in classes:
                result = self.__session.query(m_class).all()
                for ob in result:
                    key = "{}.{}".format(type(ob).__name__, ob.id)
                    r_dict[key] = ob
        return (r_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
        self.__session.commit()
        self.__session.close()

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
        self.__session.close()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
            self.__session.commit()
            self.__session.close()

    def reload(self):
        """create all tables in the database,
        create the current database session"""
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
