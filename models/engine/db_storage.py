#!/usr/bin/python3
""" Class definition for database"""
import os
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ Database storage class"""

    __engine =None
    __session = None

    def __init__(self):
        """ constructor method"""

        query = "mysql+mysqldb://{}:{}@{}/{}".format(
              os.getenv('HBNB_MYSQL_USER'),
              os.getenv('HBNB_MYSQL_PWD'),
              os.getenv('HBNB_MYSQL_HOST'),
              os.getenv('HBNB_MYSQL_DB')
        )
        self.__engine = create_engine(query, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ A method returning a dictionary"""

        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for element in query:
                key ="{}.{}".format(type(element).__name__, element.id)
                dic[key] = element
        else:
            s_list = [State, City, User, Place, Review, Amenity]
            for cs in s_list:
                query = self.__session.query(cs)
                for i in query:
                    key = "{}.{}".format(type(i).__name__, i.id)
                    dic[key] = i
        return (i)

    def new(self, obj):
        """ adds new element in table"""

        self.__session.add(obj)

    def save(self):
        """ for saving"""

        self.__session.commit()

    def delete(self, obj=None):
        """ deletes an element from table"""

        self.session.delete(obj)

    def reload(self):
        """ reloads data"""

        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session()

    def close(self):
        """ closes session"""

        self.__session.close()

