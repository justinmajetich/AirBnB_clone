#!/usr/bin/python3
"""This module instantiates an object of class DBStorage"""""
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy import Integer, String, Column, DateTime, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship


class DBStorage:
    """
    This class manages storage of hbnb models in SQL format.

    Attributes:
        __engine (sqlalchemy.engine.Engine): The database engine.
        __session (sqlalchemy.orm.Session): The database session.
    """

    def __init__(self):
        """
        Initializes a new instance of the DBStorage class.
        """
        usr = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        database = getenv('HBNB_MYSQL_DB')
        host = getenv('HBNB_MYSQL_HOST')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(usr, passwd, host, database),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.

        Args:
            cls (class, optional): The class of the models to retrieve.
            If not provided, retrieves all models.

        Returns:
            dict: A dictionary of models in the format:
            {<model_name>.<model_id>: <model_instance>}.
        """
        if cls is None:
            classes = [State, City, User, Place, Review, Amenity]
            objs = []
            for c in classes:
                objs += self.__session.query(c).all()
        else:
            objs = self.__session.query(cls).all()
        return {type(obj).__name__ + '.' + obj.id: obj for obj in objs}

    def new(self, obj):
        """
        Creates a new instance and adds it to the database.

        Args:
            obj (BaseModel): The model instance to add to the database.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the database.

        Returns:
            None
        """
        self.__session.commit()

    def reload(self):
        """
        Loads storage tables from the database.
        """
        Base.metadata.create_all(self.__engine)
        db_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(db_session)
        self.__session = Session()

    def delete(self, obj=None):
        """
        Deletes an object from the database.

        Args:
            obj (BaseModel, optional):
                The model instance to delete from the database.
        """
        if obj:
            self.__session.delete(obj)
