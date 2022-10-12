#!/usr/bin/python3
""" """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
import os
import urllib.parse

workspace = os.getenv("HBNB_ENV")
username = os.getenv("HBNB_MYSQL_USER")
passwd = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
port = 3306
db = os.getenv("HBNB_MYSQL_DB")
src = f"mysql+mysqldb://{username}:{passwd}@{host}:{port}/{db}"


class DBStorage:
    """ """
    __engine = None
    __session = None

    def __init__(self):
        """ """
        self.__engine = create_engine(src, pool_pre_ping=True)
        self.__session = sessionmaker.configure(bind=self.__engine)
        try:
            if workspace == "test":
                Base.metadata.drop_all(bind=self.__engine)
        except BaseException:
            pass

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dictionary = {}
        if cls is not None:
            for obj in self.__session.query(cls):
                dictionary.update({f"{cls}.{cls.id}": obj})
        else:
            for obj in self.__session.query(*):
                dictionary.update({f"{cls}.{cls.id}": obj})
        return dictionary

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
