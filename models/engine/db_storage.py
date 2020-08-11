#!/usr/bin/python3
"""This module defines a class to manage data base storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        DBStorage.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                           .format(getenv('HBNB_MYSQL_USER'),
                                                   getenv('HBNB_MYSQL_PWD'),
                                                   getenv('HBNB_MYSQL_HOST'),
                                                   getenv('HBNB_MYSQL_DB')),
                                           pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=DBStorage.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            my_query = DBStorage.__session.query(User,
                                                 State,
                                                 City,
                                                 Amenity,
                                                 Place,
                                                 Review).all()
            my_dict = {}
            for obj in my_query:
                my_dict.update(
                    {obj.to_dict()['__class__'] + '.' + obj.id: obj})
            return my_dict
        else:
            my_query = DBStorage.__session.query(cls).all()
            my_dict = {}
            for obj in my_query:
                my_dict.update(
                    {obj.to_dict()['__class__'] + '.' + obj.id: obj})
            return my_dict

    def new(self, obj):
        """Adds new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""

        Base.metadata.create_all(DBStorage.__engine)

        session_factory = sessionmaker(bind=DBStorage.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()

    def delete(self, obj=None):
        """
        Deletes from the current database session
        Args:
            obj ([type], optional): [description]. Defaults to None.
        """
        if obj:
            self.__session.delete(obj)
"""
            _cls = obj.__class__
            print(_cls)
            my_query = self.__session.query(_cls) \
                                     .filter(_cls.id=obj.id) \
                                     .first()
            if my_query:
                self.__session.delete(my_query)
"""
