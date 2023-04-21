#!/usr/bin/python3
"""
db_storage module
"""
from os import getenv, environ
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models


class DBStorage:
    """DB Storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation"""
        user = environ.get("HBNB_MYSQL_USER")
        passwd = environ.get("HBNB_MYSQL_PWD")
        host = environ.get("HBNB_MYSQL_HOST")
        database = environ.get("HBNB_MYSQL_DB")
        env = environ.get("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, passwd, host, database),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database"""

        obj_classes = {'City': City, 'User': User, 'State': State,
                       'Amenity': Amenity, 'Place': Place, 'Review': Review}
        db_dict = {}
        if cls is None:
            for obj_class in obj_classes.values():
                obj_list = self.__session.query(obj_class)
                for obj in obj_list:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    db_dict[key] = obj
                    del obj.__dict__['_sa_instance_state']
            return db_dict
        else:
            obj_list = self.__session.query(cls)
            for obj in obj_list:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
            return db_dict

    def new(self, obj):
        """Adds object to a current database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current database session obj"""
        if obj is not None:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """ Reload """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session
        attribute (self.__session) on the class"""
        self.__session.close()
