#!/usr/bin/python3
"""
database storage type
"""
from models.amenity import Amenity
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.user import User
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {"State": State, "City": City, "User": User}

class DBStorage:
    """
    database storage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        create a DBStorage instance
        """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine("mysql://{}:{}@{}/{}".format(HBNB_MYSQL_USER,HBNB_MYSQL_PWD,HBNB_MYSQL_HOST,HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        retrieve all obj in the db
        """
        my_dict = {}
        objs = []
        if cls is None:
            for cl in classes.values():
                objs += self.__session.query(cl).all()
            for obj in objs:
                key = obj.__class__.__name__ + "." + obj.id
                my_dict[key] = obj
            return my_dict
        else:
            objs = self.__session.query(cls).all
            for obj in objs:
                key = obj.__class__.__name__ + "." + obj.id
                my_dict[key] = obj
            return my_dict

    def new(self, obj):
        '''
        add a new obj to th db
        '''
        self.__session.add(obj)
        #self.__session.commit()

    def save(self):
        '''
        save or commit the changes
        '''
        self.__session.commit()

    def delete(self, obj=None):
        """
        deleting an obj fron the db
        """
        if obj is not None:
            self.session.remove(obj)
            self.__session.commit()

    def reload(self):
        """
        reloading the objs from
        the db
        """
        Base.metadata.create_all(self.__engine)
        fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(fact)
        self.__session = Session()

    def close(self):
        """
        doc
        """
        self.__session.remove()
