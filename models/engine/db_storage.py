#!/usr/bin/python3
""" DB Storage Engine """
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


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

    def all(self, cls=None):
        """
        Query all objects in the current session, optionally filtering by class.
        Returns a dictionary where the keys are in the format <class-name>.<object-id>
        and the values are the corresponding objects.
        """

        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

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

    def reload(self):
        """ Creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_time = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_time)
        self.__session = Session()
