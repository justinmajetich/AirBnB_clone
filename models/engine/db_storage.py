#!/usr/bin/python3

"""module"""

from sqlalchemy import text
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None, id=None):
        """all method"""
        classes = [User, State, City, Amenity, Place, Review]
        new_dict = {}

        if cls is not None:
            if id is not None:
                key = cls.__name__ + '.' + id
                obj = self.__session.query(cls).get(id)
                new_dict[key] = obj
            else:
                # Use text('class_name') to explicitly declare the class name
                class_name_expr = text(cls.__name__)
                for obj in (self.__session.query(cls).filter
                            (class_name_expr == class_name_expr)):
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        else:
            for c in classes:
                # Use text('class_name') to explicitly declare the class name
                class_name_expr = text(c.__name__)
                for obj in (self.__session.query(c).filter
                            (class_name_expr == class_name_expr)):
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """new method"""
        self.__session.add(obj)

    def save(self):
        """save method"""
        with self.__session as session:
            session.commit()

    def delete(self, obj=None):
        """delete method"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload method"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close method"""
        self.__session.close()
