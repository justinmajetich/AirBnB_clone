#!/usr/bin/python3
"""
New engine DBStorage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new instance of DBStorage"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    user, password, host, database), pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        que_dict = {}
        obj_list = [User, State, City, Amenity, Place, Review]
        if cls is not None:
            for obj1 in obj_list:
                for obj2 in self.__session.query(obj1).all():
                    que_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj2
        else:
            for obj in self.__session.query(cls).all():
                que_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return(que_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(new_session)
