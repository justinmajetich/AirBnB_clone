#!/usr/bin/python3
"""DB Storage"""
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.engine.file_storage import FileStorage
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


class DBStorage(FileStorage):
    """MySQL database interaction"""
    __engine = None
    __session = None
    _FileStorage__objects = {}

    def __init__(self):
        """ Initialize instance of DBStorage """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".
            format(getenv("HBNB_MYSQL_USER"),
                   getenv("HBNB_MYSQL_PWD"),
                   getenv("HBNB_MYSQL_HOST"),
                   getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Re-Wrote function completely """
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            objects = self.__session.query(cls)
        else:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(Amenity).all())
        my_dict = {}
        for obj in objects:
            my_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return my_dict

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
        """ Restructures the session """
        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()

    def close(self):
        """ Calls removes() on private session attr (self.__session) """
        self.__session.close()
