#!?usr/bin/python3
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from sqlalchemy .orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
class DBStorage:
    """ Creates the environment in the tables """
    __engine  = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                        .format(user, password, host, db), 
                        pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary
        Return:
            return a dictionary of __object
        """
        my_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for item in query:
                key = "{}.{}.",format(type(elem).__name__, item.id)
                my_dict[key] = item
        else:
            my_class = [State, City, User, Place, Review, Amenity]
            for clazz in my_class:
                query = self._session.query(clazz)
                for item in query:
                    key = "{}.{}".format(type(item).__class, item.id)
                    my_dict[key] = item
        return (my_dict)


    def new(self, obj):
        """ add a new element in the table
        """
        self.__Session.add(obj)

    def save(self):
        """ save change
        """
        self.__session.commit()

    def reload(self):
        """ starting the engine
        """
        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine, 
                    expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()
