import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base  # Import the Base class first
from models.user import User  # Import the User class after Base and before the other models
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models

class DBStorage:
    """engine DBStorage connecting to MysqlAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """The init method that initializes an engine"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))

    def all(self, cls=None):
        """A method that gets all the objects of cls if not
        None, then it gets all the objects of all classes"""
        allObjects = {}
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]
        for cls in classes:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                allObjects[key] = obj
        self.__session.close()
        return allObjects

    def new(self, obj):
        """A method that adds an obj to the current database
        session"""
        self.__session.add(obj)

    def save(self):
        """A method that commits the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """A method that deletes the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """A method that reloads a session. saves all the tables
        and it uses scoped session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
