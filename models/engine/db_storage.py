#!/usr/bin/python3
"""Definition of the DBStorage class."""
from ast import literal_eval
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Represents a DBStorage object.

    Args:
        __engine: The current sqlalchemy engine.
        __session: The current sqlalchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialiazes a database."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary containing depending key: object
           pairs on the cls provided."""
        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(Amenity).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Review).all())

        else:
            objects = self.__session.query(cls).all()
        return {"{}.{}".format(type(object).__name__, object.id): object
                for object in objects}

    def new(self, obj):
        """Adds the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database."""
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
