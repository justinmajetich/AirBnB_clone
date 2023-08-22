#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage():
    """This class manages storage of hbnb models in an SQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the SQL db storage"""
        from models.base_model import Base

        db_host = os.environ.get('HBNB_MYSQL_HOST')
        db_user = os.environ.get('HBNB_MYSQL_USER')
        db_password = os.environ.get('HBNB_MYSQL_PWD')
        db_name = os.environ.get('HBNB_MYSQL_DB')
        mode = os.environ.get('HBNB_ENV')

        self.__engine = create_engine(
            f'mysql+mysqldb://{db_user}:{db_password}@{db_host}/{db_name}',
            pool_pre_ping=True)
        if (mode == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from console import HBNBCommand
        from models.base_model import BaseModel

        object_dict = {}
        if cls is None:
            for key in HBNBCommand.classes:
                if key != "BaseModel":
                    val = HBNBCommand.classes[key]
                    for row in self.__session.query(val).all():
                        object_dict.update({f'{key}.{row.id}': row})
            return object_dict
        else:
            if cls is not BaseModel:
                for row in self.__session.query(cls).all():
                    object_dict.update({f'{cls}.{row.id}': row})
            return object_dict

    def new(self, obj):
        """Creates a new object"""
        self.__session.add(obj)

    def save(self):
        """Saves session to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the database"""
        if not obj:
            return
        self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session()

    def close(self):
        """Resets the session from the database"""
        self.__session.close()
