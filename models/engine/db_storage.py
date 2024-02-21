#!/usr/bin/python3
""" Database Storage engine """
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
        class of the storage engine
    """
    __engine = None
    __session = None
    classes = [
        City,
        State,
        User,
        Review,
        Place,
        Amenity
    ]

    def __init__(self) -> None:
        """ Constructor Function """

        user, passwd = getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD')
        host, db = getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            gets all the class object in storage

            Args:
                cls: class to get all objects
        """

        new_dict = dict()
        if cls:
            rows = self.__session.query(cls).all()

            for obj in rows:
                new_dict[cls.__name__ + '.' + obj.id] = obj
            return new_dict

        for classname in self.classes:
            rows = self.__session.query(classname).all()

            for obj in rows:
                new_dict[classname.__name__ + '.' + obj.id] = obj

        return new_dict

    def new(self, obj):
        """
            Starts a new session or transaction

            Args:
                obj: object to be added
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Saves the transaction """
        self.__session.commit()

    def delete(self, obj=None):
        """
            delete from the current db session obj if not none
        """
        if obj:
            self.__session.delete()

    def reload(self):
        """
            reload the session so far
        """
        Base.metadata.create_all(self.__engine)

        ses_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses_factory)
        self.__session = Session()

    def close(self):
        """
            removes the private session
        """
        self.__session.close()
