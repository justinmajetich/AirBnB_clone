#!/usr/bin/python3
"""DBStorage class for AirBnB."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """DBStorage."""

    __engine = None
    __session = None

    def __init__(self):
        """Init method."""
        mysql_user = getenv('HBNB_MYSQL_USER')
        mysql_pwd = getenv('HBNB_MYSQL_PWD')
        mysql_host = getenv('HBNB_MYSQL_HOST')
        mysql_db = getenv('HBNB_MYSQL_DB')
        mysql_env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            mysql_user, mysql_pwd, mysql_host, mysql_db), pool_pre_ping=True)

        """If var HBNB_ENV == test, then DROP all the tables."""
        if mysql_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """All method - retrieves an object representation.
        Args:
            cls [object]: Instance of a class.
        Return:
            new_dict [dict]: Dictionary with all object representations.
        """
        if cls is not None:
            objs = self.__session.query(cls).all()

        else:
            classes = ['State', 'City', 'User', 'Place', 'Review', 'amenity']
            objs = []
            for _class in classes:
                objs += self.__session.query(eval(_class)).all()

        """creating a new dictionary and saving data"""
        new_dict = {}

        for obj in objs:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """Add the object to the current. database session (self.__session)."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current. database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database (feature of SQLAlchemy)."""
        Base.metadata.create_all(self.__engine)

        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)

        Session = scoped_session(self.__session)
        self.__session = Session()