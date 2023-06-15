#!/usr/bin/python3
"""New engine DBStorage"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """The new database storage class"""
    _engine = None
    _session = None

    def __init__(self):
        """Initialize the DBStorage class"""
        self._engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                     .format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                     pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self._engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        classes = [User, State, City, Place, Amenity, Review]
        new_dict = {}
        if cls is None:
            for c in classes:
                for obj in self._session.query(c).all():
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        else:
            for obj in self._session.query(cls).all():
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Adds a new object to the database"""
        self._session.add(obj)

    def save(self):
        """Saves all changes to the database"""
        self._session.commit()

    def delete(self, obj=None):
        """Deletes an object from the database"""
        if obj is not None:
            self._session.delete(obj)

    def reload(self):
        """Reloads all tables"""
        Base.metadata.create_all(self._engine)
        session_factory = sessionmaker(bind=self._engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self._session = Session()

    def close(self):
        """Close the session"""
        self._session.close()
