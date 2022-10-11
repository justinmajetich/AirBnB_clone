#!/usr/bin/python3
"""
    This defines the engine for the database
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

# Models from model Package
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

# Global Class Dictionary
classes = {
    "User": User,
    "State": State,
    "City": City,
    "Place": Place,
    "Amenity": Amenity,
    "Review": Review
}


class DBStorage:
    """
        Database storage engine for MySQL
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            Instantiates a dbstorage instance

            Environment Params:
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST, HBNB_MYSQL_DB,
                HBNB_ENV
        """
        db_string = 'mysql+mysqldb://{}:{}@{}/{}'
        db_user = getenv('HBNB_MYSQL_USER')
        db_host = getenv('HBNB_MYSQL_HOST')
        db_pwd = getenv('HBNB_MYSQL_PWD')
        db_name = getenv('HBNB_MYSQL_DB')
        db_env = getenv('HBNB_ENV')

        self.__engine = create_engine(db_string.format(
            db_user,db_pwd,db_host, db_name
        ))

        if db_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """
            Adds new object to session to be commited
            to db
        """
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """
            Commits all changes to db session
        """
        self.__session.commit()


    def reload(self):
        """
            reloads database
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(session)()

    def close(self):
        """
            Closes the working SQLAlchemy session
        """
        self.__session.close()

    def delete(self, obj=None):
        """
            Deletes from the current database session obj
        """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id
            ).delete()
