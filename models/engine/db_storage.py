#!/usr/bin/python3
''' Define the DBStorage engine '''
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, scoped_session
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classname = {"User": User, "State": State, "City": City,
             "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    ''' Instantiate the DBStorage object '''
    __engine = None
    __session = None

    def __init__(self):
        ''' Instantiate the DBStorage Instance '''
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV = 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ''' Return all the elements or the ones with the classnale cls '''
        output = {}
        if cls is None:
            for name in classname.values():
                obj_list = self.__session.query(name).all()
        else:
            obj_list = self.__session.query(cls).all()
        for obj in obj_list:
            key = obj.__class__.__name__ + '.' + obj.id
            output[key] = obj
        return output

    def new(self, obj):
        ''' Adding obj to the current database session '''
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        ''' Saving the changes made to the current database session '''
        self.__session.commit()
        self.__session.close()

    def delete(self, obj=None):
        ''' Delete obj from the current database session '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        ''' create all tables in the database and create the
            current database session '''
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        self.__session = scoped_session(session_maker)()
