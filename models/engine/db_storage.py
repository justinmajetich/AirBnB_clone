#!/usr/bin/python3

"""
"""

from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import classes
import models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """
    """
    __engine = None
    __Session = None

    def __init__(self):
        """
        create/initialize the engine
        """
        conn = "mysql+mysqldb://{}:{}@{}:3306/{}"
        __engine = create_engine(conn.format(
                                            os.getenv("HBNB_MYSQL_USER"),
                                            os.getenv("HBNB_MYSQL_PWD"),
                                            os.getenv("HBNB_MYSQL_HOST"),
                                            os.getenv("HBNB_MYSQL_DB"),
                                            pool_pre_ping=True))
        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query the current database session
        """
        myDict = {}
        if (cls is not None):
            queryData = self.__session.query(cls.__class__.__name__).all()
            for data in queryData:
                key = "{}.{}".format(data.__class__.__name__, data.id)
                myDict[key] = data
            return myDict
        else:
            for key, value in classes.items():
                if (key != "BaseModel"):
                    queryData = self.session.query(value).all()
                    if (queryData):
                        for (data in queryData):
                            key = "{}.{}".format(data.__class__.__name__, data.id)
                            myDict[key] = data
            return myDict

    def new(self, obj):
        """
        add object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit changes made to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if (obj is not None):
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the databsse
        cerate the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
