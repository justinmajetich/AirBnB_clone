#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import sqlalchemy
import json
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
os.environ['HBNB_MYSQL_USER'] = 'user'
os.environ['HBNB_MYSQL_PWD'] = 'password'
os.environ['HBNB_MYSQL_HOST'] = 'host'
os.environ['HBNB_MYSQL_DB'] = 'database'

classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }


class DBStorage():
    __engine = None
    __session = None
    __objects = {}

    def __init__(self):
        self.__engine = sqlalchemy.create_engine(
             "mysql://{}:{}@localhost/{}".format('HBNB_MYSQL_USER', 'HBNB_MYSQL_PWD', 'HBNB_MYSQL_DB'),
            pool_pre_ping=True)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        self.user = self.__session.query(User)
        self.state = self.__session.query(State)
        self.city = self.__session.query(City)
        self.amenity = self.__session.query(Amenity)
        self.place = self.__session.query(Place)
        self.review = self.__session.query(Review)

        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            spec_dict = {}
            for key, val in self.__objects.items():
                if cls == type(val):
                    spec_dict[key] = val
            return spec_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        self.__session.new(self)
        self.__session.save()

    def delete(self, obj=None):
        """deletes current instance from the storage"""
        if obj is not None:
            self.__session.new(self)
            self.__session.delete()

    def reload(self):
        """Loads storage dictionary from file"""

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker, expire_on_commit=False)

        try:
            temp = {}
            with open(DBStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
