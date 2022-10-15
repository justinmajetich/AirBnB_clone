#!/usr/bin/python3
""" Database Storage using sqlalchemy ORM to map classes to MySQL. """
from ast import Delete
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
import urllib.parse


workspace = os.getenv("HBNB_ENV")
username = os.getenv("HBNB_MYSQL_USER")
passwd = urllib.parse.quote_plus(os.getenv("HBNB_MYSQL_PWD"))
host = os.getenv("HBNB_MYSQL_HOST")
port = 3306
db = os.getenv("HBNB_MYSQL_DB")
src = f"mysql+mysqldb://{username}:{passwd}@{host}:{port}/{db}"
Session = sessionmaker()


class DBStorage:
    """ This class manages storage of hbnb models in MySQL database """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor to initialize sqlalchemy sessions
            from the database connection
        """
        self.__engine = create_engine(src, pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session.configure(bind=self.__engine)
        self.__session = Session()
        try:
            if workspace == "test":
                Base.metadata.drop_all(bind=self.__engine)
        except BaseException:
            pass

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dictionary = {}
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            if cls:
                for obj in self.__session.query(cls):
                    dictionary.update({f"{cls}.{obj.id}": obj.to_dict()})
            else:
                for class_name in classes.values():
                    instance = self.__session.query(class_name).one_or_none()
                    if instance:
                        for obj in self.__session.query(class_name).all():
                            dictionary.update({f"{class_name}.{obj.id}": obj})
        except Exception:
            pass
        finally:
            return dictionary

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        scope = Session.configure(bind=self.__engine,
                                  expire_on_commit=False)
        self.__session = scoped_session(scope)

    def delete(self, obj=None):
        """ Deletes object from __objects """
        if obj:
            self.__session.delete(obj)
            self.save()
