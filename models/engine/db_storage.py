#!/usr/bin/python3
"""DBStorage class definition"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
import datetime


class DBStorage():
    """ DB storage class definition"""
    __engine = None
    __session = None

    def __init__(self):
        """init storage engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        """drop all tables if the environment variable HBNB_ENV is equal to test"""

    def all(self, cls=None):
        """get all db instances"""
        if cls:
            objs = self.__session.query(eval(cls))
        else:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Review).all()

        obj_dic = {}
        for obj in objs:
            k = '{}.{}'.format(type(obj).__name__, obj.id)
            obj_dic[k] = obj
        return(obj_dic)

    def new(self, obj):
        """add obj to current session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to db sess"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from db session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in db
            create current db session"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()



