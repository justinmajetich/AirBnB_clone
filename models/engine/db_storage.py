#!/usr/bin/python3
"""DBStorage class for AirBnB Clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """DBStorage class for AirBnB Clone"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance"""
        db_user = os.environ.get('HBNB_MYSQL_USER')
        db_pwd = os.environ.get('HBNB_MYSQL_PWD')
        db_host = os.environ.get('HBNB_MYSQL_HOST')
        db_name = os.environ.get('HBNB_MYSQL_DB')
        db_env = os.environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(db_user, db_pwd, db_host, db_name),
                                      pool_pre_ping=True)

        if db_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects in the database"""
        obj_dict = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls is not None:
            if cls in classes:
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    obj_dict[key] = obj
            return obj_dict

        for c in classes:
            query_result = self.__session.query(c).all()
            for obj in query_result:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.close()
