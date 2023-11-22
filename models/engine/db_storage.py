#!/usr/bin/python3
"""
Defines DBStorage engine
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


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
        classes = [cls] if cls else [User, State, City, Amenity, Place, Review]

        for class_obj in classes:
            objects = self.__session.query(class_obj).all()
            for obj in objects:
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

