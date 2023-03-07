#!/usr/bin/python3

"""contains the class db_storage"""

import os

from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City


class DBStorage:
    """This is the Database Storage Engine class"""
    __engine = None
    __session = None

    """
    set env variables depending on your OS
    """

    def __init__(self):
        """initialize object"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = sqlalchemy.create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(user,
                    password,
                    host,
                    database), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == "test":
            # from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieves all objects in Database queried based on clas"""

        classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        obj_dict = {}
        if cls is not None and cls in classes:
            class_objects = self.__session.query(classes[cls]).all()
            for obj in class_objects:
                key = obj.__class__.__name__ + "." + obj.id
                obj_dict[key] = obj

        if cls is None:
            for cls in classes:
                class_objects = self.__session.query(classes[cls]).all()
                for obj in class_objects:
                    key = obj.__class__.__name__ + "." + obj.id
                    obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """adds the object to the current session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = session()
