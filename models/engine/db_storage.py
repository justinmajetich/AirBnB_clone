#!/usr/bin/python3
"""."""

from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import relationship


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                             format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST '),
                                             getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            objs = self.__session.query(User).all()
            objs.extend = (self.__session.query(State).all())
            objs.extend = (self.__session.query(City).all())
            objs.extend = (self.__session.query(Amenity).all())
            objs.extend = (self.__session.query(Place).all())
            objs.extend = (self.__session.query(Review).all())
        else:
            if type(cls) == str:
                objs = self.__session.query(cls)
        dict = {"{}.{}".format(obj.__class__.name__, obj.id):\
                               obj for obj in objs}
        return dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self, obj):
        self.__session.commit()

    def delete(self, obj):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
