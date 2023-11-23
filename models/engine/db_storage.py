#!/usr/bin/python3
"""
Defines DBStorage engine
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity

classes = {
        "State": State,
        "City": City
        }

class DBStorage:
    """
    class DBStorage for managing Database records
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance"""
        self.__engine = create_engine(self.get_engine_url(), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def get_engine_url(self):
        """
        Generate the db engine url based on env variables
        """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        return f'mysql+mysqldb://{user}:{password}@{host}/{database}'

    def close(self):
        """Close the session"""
        if self.__session:
            self.__session.remove()

    def all(self, cls=None):
        """
        Query all objects depending on the class name
        """
        result = {}
        if cls is None:
            for class_name in classes.values():
                objs = self.__session.query(class_name).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    result[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result[key] = obj
        return result

    def new(self, obj):
        """
        Add the object to the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from the current databse sessions if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and the current session
        """
        Base.metadata.create_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

