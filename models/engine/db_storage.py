#!/usr/bin/python3
""" Storage info to the data base"""


from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


os.environ["HBNB_MYSQL_USER"] = 'hbnb_dev'
os.environ["HBNB_MYSQL_PWD"] = 'hbnb_dev_pwd'
os.environ["HBNB_MYSQL_HOST"] = 'localhost'
os.environ["HBNB_MYSQL_DB"] = 'hbnb_dev_db'


class DBStorage():
    """ Data Base Class """
    __engine = None
    __session = None

    def __init__(self):
        """Instantation for the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Return dictionary of all the objects in the file """
        table_dict = {}
        classes = {
            'State': State,
            'City': City,
            'User': User}
        if cls is None:
            for c in classes:
                result = self.__session.query(classes[c]).all()
                for obj in result:
                    table_dict[f"{type(obj).__name__}.{obj.id}"] = obj
        else:
            result = self.__session.query(classes[cls]).all()
        for obj in result:
            table_dict[f"{type(obj).__name__}.{obj.id}"] = obj
        return table_dict

    def new(self, obj):
        " add the object to the current database session "
        self.__session.add(obj)

    def save(self):
        " Commit all changes of hte current database session "
        self.__session.commit()

    def delete(self, obj=None):
        " delete form the current database session"
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        " Create all tables in the database, and creates the current session "
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """ closes session"""
        self.__session.close()
