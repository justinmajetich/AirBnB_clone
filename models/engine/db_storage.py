#!/usr/bin/python3
'''Database storage engine'''
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import os

classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

        try:
            with self.__engine.connect() as conn:
                result = conn.execute(text("SELECT 1"))
                # print("✅ Connection successful:", result.scalar())
        except Exception as e:
            pass
            # print("❌ Connection failed:", e)

    def all(self, cls=None):
        """Queries the current session and list all instances of cls"""
        instances = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                instances[key] = obj
        else:
            for obj_cls in classes.values():
                objs = self.__session.query(obj_cls).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    instances[key] = obj
        return instances

    def new(self, obj):
        """Adds object to current session"""
        self.__session.add(obj)

    def save(self):
        """Saves current work done"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the current obj in the database session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
           - Makes sure all tables exist in the db.
           - Sets up factory for creating sessions, with objects not expring
             after commit
           - Wraps session_factory in a thread-safe helper
           - Creates a new session and stores it in self.__session for later
             use
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Connections are returned back to the connection pool creating
           an empty scoped_session object and will create a new Session when
           called again.
        """
        self.__session.close()
