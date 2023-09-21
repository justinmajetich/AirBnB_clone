#!/usr/bin/python3
"""model containing database for storage"""

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

classes = {"State": State, "City": City, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    """classe that defines dbstorage instances"""

    __engine = None
    __session = None

    def __init__(self):
        """function that initializes public instances"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host,
                                              database), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns models of current database"""
        dictionary = {}
        if cls is None:
            for elem in classes.values():
                objs = self.__session.query(elem).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dictionary[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """function that adds object to database"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as error:
                self.__session.rollback()
                raise error

    def save(self):
        """function that commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """function that create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        se_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(se_factory)()

    def close(self):
        """function that closes current database"""
        self.__session.close()