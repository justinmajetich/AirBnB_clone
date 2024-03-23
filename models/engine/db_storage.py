#!/usr/bin/python3
"""
DBStorage: Manages hbnb model storage using SQLAlchemy and MySQL.
"""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import IntegrityError

from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in SQLAlchemy format"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new DBStorage engine"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db),
            pool_pre_ping=True,
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the current database session based on class name"""
        new_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for class_ in classes:
                objs = self.__session.query(class_).all()
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        try:
            self.__session.commit()
        except IntegrityError as e:
            print(f"Error: {e}")
            self.__session.rollback()

    def delete(self, obj=None):
        """Deletes obj from the current database session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False
                )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the current database session"""
        self.__session.close()
