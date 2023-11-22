#!/usr/bin/python3
"""database storage engine"""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, class_mapper
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.user import User
from models.amenity import Amenity

user = os.environ['HBNB_MYSQL_USER'] if 'HBNB_MYSQL_USER' in os.environ else None
password = os.environ['HBNB_MYSQL_PWD'] if 'HBNB_MYSQL_PWD' in os.environ else None
host = os.environ['HBNB_MYSQL_HOST'] if 'HBNB_MYSQL_HOST' in os.environ else None
database = os.environ['HBNB_MYSQL_DB'] if 'HBNB_MYSQL_DB' in os.environ else None
test = os.environ['HBNB_ENV'] if 'HBNB_ENV' in os.environ else None

class DBStorage():
    """database engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initialisation"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), pool_pre_ping=True)
        if test == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        self.__session = Session()


    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objects = dict()
        all_classes = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_type in all_classes:
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects

    def new(self, obj):
        """adds new object to the database"""
        self.__session_add(obj)

    def save(self):
        """commits changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):

        """deletes object in the current session"""
        self.__session.delete(obj)
        self.save()

    def reload(self):
        """creates all tables in the database"""
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)
