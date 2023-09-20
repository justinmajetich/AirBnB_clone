#!/usr/bin/python3
"""database configuration"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import create_engine
from os import getenv
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.place import Place
from models.city import City


class DBStorage:
    """Defines the database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database storage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Provides access to all objects"""
        objs = []
        if cls is None:
            Classes = [State, City, Place, Review, Amenity, User]
        try:
            for Class in Classes:
                objs = objs + self.__session.query(Class).all()
        except Exception:
            pass
        else:
            Class = eval(cls) if isinstance(cls, str) else cls
        objs = self.__session.query(Class).all()
        return {'{}.{}'.format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Provides a new instance of the class"""
        self.__session.add(obj)

    def save(self):
        """Allows the class to be saved"""
        self.__session.commit()

    def delete(self, obj=None):
        """Allows the class to be deleted"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Allows the class to be reloaded"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Provides shutdown functionality"""
        self.__session.close()
