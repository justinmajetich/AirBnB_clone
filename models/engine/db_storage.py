"""Engine for the database storage
"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity

class DBstorage:
    __engine = None
    __session = None

    def __init__(self):
        """create the engine 
        """
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_psw = getenv("HBNB_MYSQL_PWD")
        mysql_host = getenv("HBNB_MYSQL_HOST", "localhost")
        mysql_db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(mysql_user, mysql_psw,
                                              mysql_host, mysql_db),
                                              pool_pre_ping=True)
        
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all
        objects depending of the class name (argument cls)
        """
        classes = [Amenity, State, City, Place, Review, User]
        objects = {}
        if cls is not None:
            query_set = self.__session(cls).all()
            for query in query_set:
                key = "{}.{}".format(type(query).__name__, query.id)
                objects[key] = query
        else:
            if cls in classes:
                query_set = self.__session(eval(cls)).all()
                for query in query_set:
                    key = "{}.{}".format(cls, query.id)
                    objects[key] = query

        return objects

    def new(self, obj):
        """add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)
        create the current database session (self.__session) from the engine
        (self.__engine) by using a sessionmaker - the option expire_on_commit must be set to False;
        and scoped_session - to make sure your Session is thread-safe
        """
        Base.metadata.create_all(self.__engine)
        self.__Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        """close the session
        """
        self.__session.close()




