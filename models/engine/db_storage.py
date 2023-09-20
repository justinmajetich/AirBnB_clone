#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}

class DBStorage:
    """database storage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        DBStorage class instances 
        """
        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB")
        )
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """return a dictionary
        """
        objs = {}
        if cls is None:
            for clas in Base.__subclasses__():
                table = self.__session.query(clas).all()
                for obj in table:
                    key = "{}.{}".format(obj.__class__.__name__,obj.id)
                    objs[key] = obj
        else:
            for obj in self.__session.query(classes[cls]).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objs[key] = obj
        return objs

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        and create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
