#!/usr/bin/python3
""" DB Storage Engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity


class DBStorage:
    """ This is our database storage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize new instance of DBStorage """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """ Creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def all(self, cls=None):
        """
        Query all objects in the current session, optionally
        filtering by class. Returns a dictionary where the keys
        are in the format <class-name>.<object-id> and the values
        are the corresponding objects.
        """
        cls_list = ["Reviews", "City", "State", "User",
                    "Place", "Amenity"]
        obj_list = []
        if cls is None:
            for cls_name in cls_list:
                obj_list.extend(self.__session.query(cls_name).all())

        else:
            if type(cls) == str:
                cls = eval(cls)
            obj_list = self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__,
                               obj.id): obj for obj in obj_list}

    def new(self, obj):
        """ Add object to current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from current database session """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """
        Ends private session
        """
        self.__session.close()

    def total(self):
        return len(self.__session.query(Review).all())
