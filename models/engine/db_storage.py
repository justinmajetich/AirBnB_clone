#!usr/bin/python3
"""Defines a new class DBStorage"""
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DBStorage:
    """Describes a new class for Database storage

    Attributes:
        __engine (sqlalchemy.Engine): The current engine.
        __session (sqlalchemy.Session): The current session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initializes new instance of DBStorage"""

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a list of specified Class or All classes"""

        cls_d = {}
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            cls_d = self.__session.query(cls).all()
        else:
            cls_d = self.__session.query(State).all()
            cls_d.extend(self.__session.query(City).all())
            cls_d.extend(self.__session.query(User).all())
            cls_d.extend(self.__session.query(Amenity).all())
            cls_d.extend(self.__session.query(Place).all())
            cls_d.extend(self.__session.query(Review).all())
        return {"{}.{}".format(type(ob).__name__, ob.id): ob for ob in cls_d}

    def new(self, obj):
        """Creates a new object in current database session"""

        self.__session.add(obj)

    def delete(self, obj=None):
        """Deletes an Object, if it exists"""

        if obj is not None:
            self.__session.delete(obj)

    def save(self):
        """Saves changes to the session"""

        self.__session.commit()

    def reload(self):
        """Creates a session in the database"""

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """ Close the current session. """
        self.__session.close()
