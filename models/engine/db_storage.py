#!/usr/bin/python3
""" Storages """

from models.base_model import BaseModel, Base
from models.state import state
from sqlalchemy import Column, String, ForeignKey, DateTime
from models.city import city
from os import getenv

class DBStorage:
    """ DB Storage """
    __engine = None
    __session = None

    def __init__(self):
        """ Method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                            getenv('HBNB_MYSQL_USER'),
                            getenv('HBNB_MYSQL_PWD'),
                            getenv('HBNB_MYSQL_HOST'),
                            getenv('HBNB_MYSQL_DB')),
                            pool_pre_ping=True)
        
        if getenv('HBNB_ENV') == 'test'
                    Base.metadata.drop_all(self.__engine)

    def all(self, cls=None)
        if cls is not None:
            self.__session.query(cls).all()
        else:
            self.__session.query(User).all()
            self.__session.query(State).all()
            self.__session.query(City).all()
            self.__session.query(Amenity).all()
            self.__session.query(Place).all()
            self.__session.query(Review).all()

