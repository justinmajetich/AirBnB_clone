#!usr/bin/python3
"""Defines a new class DBStorage"""
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DBStorage:
    """Describes a new class for Database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes new instance of DBStorage"""

        user = os.environ.get('HBNB_MYSQL_USER')
        passwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        env_check = os.environ.get('HBNB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}\
                                      @{host}:3306/{db}', pool_pre_ping=True)

        if env_check == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a list of specified Class or All classes"""

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker()
        Session.configure(bind=self.__engine)
        self.__session = Session()

        cls_dict = {}
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            cls_dict = self.__session.query(cls).all()
            return cls_dict
        else:
            cls_dict = self.__session.query(State).all()
            cls_dict.extend(self.__session.query(City).all())
            cls_dict.extend(self.__session.query(User).all())
            cls_dict.extend(self.__session.query(Amenity).all())
            cls_dict.extend(self.__session.query(Place).all())
            cls_dict.extend(self.__session.query(Review).all())
            return cls_dict
