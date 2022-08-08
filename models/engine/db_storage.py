""" new engine DBStorage"""
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """new engine DBStorage"""
    __engine = ""
    __session = ""


def __init__(self):
    """create the engine """
    user = os.getenv("HBNB_MYSQL_USER")
    password = os.getenv("HBNB_MYSQL_PWD")
    host = os.getenv("HBNB_MYSQL_HOST")
    database = os.getenv("HBNB_MYSQL_DB")
    self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                  .format(user, password, host,
                                          database), pool_pre_ping=True)
    if os.getenv("HBNB_ENV") == 'test':
        Base.metadata.drop_all(self.__engine)


def all(self, cls=None):
    """query on the current database session
    all objects depending of the class name
    if cls=None
    query all types of objects"""

    db_dict = {}
    objects_list = {User, State, City, Amenity, Place, Review}
    if cls is not None:
        for cls in objects_list:
            result = self.__session.query(cls).all()
            for obj in result:
                key = obj.__class__.__name__ + '.' + obj.id
                db_dict[key] = obj
    return db_dict


def new(self, obj):
    """add the object to the current database session"""
    self.__session.add(obj)


def save(self):
    """commit all changes of the current database session"""
    self.__session.commit(obj)


def delete(self, obj=None):
    """delete from the current database session obj if not None"""
    if obj not None:
        self.__session.delete(obj)


def reload(self):
    """create all tables in the database
    create the current database session from engine"""
    Base.metadata.create_all(self.__engine)
    Session = scoped_session(sessionmaker(bind=self.__engine,
                                          expire_on_commit=False))
    self.__session = Session()
