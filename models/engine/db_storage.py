#!/usr/bin/python3
"""
Defines the Dbstorage engine
"""

from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity


class DBStorage:
    """
    Represents the database storage engine

    Attributes:
    __engine: the sqlalchemy's engine
    __session: the sqlalchemy's session

    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the DbStorage instance
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session of the class.

        If cls is None, queries all types of objects.

        Return:
            dict classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(h).__name__, h.id): h for h in objs}

    def new(self, obj):
        """Adding objects to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit/save all changes to the current db session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes objects from the current db session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create the tables in the db and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes session."""
        self.__session.close()
