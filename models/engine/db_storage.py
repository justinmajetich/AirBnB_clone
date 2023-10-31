#!/usr/bin/python3
"""DB Storage"""
from os  import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class DBStorage:
    """MySQL database interaction"""
    __engine = None
    __session = None


    def __init__(self):
        """Initialize instance of DBStorage"""

        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}'f'\
                                      @{host}/{database}', pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current DB"""
        dictt = {}
        for typeClass in classes.keys():
            if cls == typeClass or cls == classes[typeClass] or cls is None:
                objs = self.__session.query(classes[typeClass]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    dictt[key] = obj
        return dictt

    def new(self, obj):
        """adding obj to db sesh"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to db sesh"""
        self.__session.commit()

    def delete(self, obj=None):
        """deleting from current db sesh obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
