#!/usr/bin/python3
""" New engine DBStorage """
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """ Database Class """

    __engine = None
    __session = None

    def __init__(self):
        """ Constructor method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True))
        if getenv('HBNB_MYSQL_TEST') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Retrieve all in a Dict or depending of parameter class"""

        if cls:
            objs = self.__session.query(self.classes()[cls])
        else:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Review).all()
        dic = {}
        for obj in objs:
            k = '{}.{}'.format(type(obj).__name__, obj.id)
            dic[k] = obj
        return dic

    def new(self, obj):
        """New object in database"""
        self.__session.add(obj)

    def save(self):
        """save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete objetc from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creating all tables"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
