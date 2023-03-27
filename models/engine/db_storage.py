#!/usr/bin/python3
""""""
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City, "Place": Place, "Review": Review,
                   "State": State, "User": User}


class DBStorage:
    """"""
    __engine = None
    __session = None

    def __init__(self):
        """"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        # Engine creation
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """All method"""
        my_dict = {}

        if cls is None:
            for my_type in classes.keys():
                for obj in self.__session.query(classes[my_type]).all():
                    key = obj.__class__.__name__ + '.' + obj.id
                    my_dict[key] = obj
        else:
            if isinstance(cls, str):
                cls = classes[cls]
            for obj in self.__session.query(cls).all():
                key = obj.__class__.__name__ + '.' + obj.id
                my_dict[key] = obj

        return my_dict

    def new(self, obj):
        """"""
        self.__session.add(obj)

    def save(self):
        """"""
        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """"""
        Base.metadata.create_all(self.__engine)
        newSession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(newSession)
        self.__session = Session

    def close(self):
        """Closes scoped session"""
        self.__session.close()