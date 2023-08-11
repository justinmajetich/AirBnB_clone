#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy import MetaData
from models.state import State
from models.user import User
import os
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review


sql = 'mysql+mysqldb://{}:{}@{}:3306/{}'
host = getenv("HBNB_MYSQL_HOST")
pssw = getenv("HBNB_MYSQL_PWD")
user = getenv("HBNB_MYSQL_USER")
db = getenv("HBNB_MYSQL_DB")

class DBStorage:
    """This class manages an engine"""
    __engine = None
    __session = None

    def __init__(self):
        """for da DBStorage"""
        self.__engine = create_engine(f"mysql+mysqldb://{us}:{ps}@{ho}/{db}",
                                      pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        """ssession database"""
        dicty = {}
        if cls:
            query_list = self.__session.query(cls).all()
            for elem in query_list:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dicty[key] = elem
        else:
            objs = [State, City, User, Place, Review]
            for i in objs:
                print(i)
            for obj in objs:
                quer = self.__session.query(obj)
                for elem in quer:
                    key ="{}.{}".format(type(elem).__name__, elem.id)
                    dicty[key] = elem

        return dicty

        def new(self, obj):
            self.__session.add(obj)

        def save(self):
            self.__session.commit()

        def delete(self, obj=None):
            if obj is not None:
                self.__session.delete(obj)

        def reload(self):
            """Loads storage dictionary from a database"""
            self.__session = Base.metadata.create_all(self.__engine)
            sess_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
            Session = scoped_session(sess_factory)
            self.__session = Session()

        def close(self):
            """ close session """
            self.__session.close()

