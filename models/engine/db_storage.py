#!/usr/bin/python3
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
""" create class dbs storage """

database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
password = getenv("HBNB_MYSQL_PWD")
hbnb_env = getenv("HBNB_ENV")

class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format
                                      (user, password, host, database),
                                      pool_pre_ping=True)
        
        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Returns a dictionary of models currently in db_storage"""
        if cls is None:
            new_dict = {}
            new_query = DBStorage.__session.query(User, State, City,
                                                 Amenity, Place, Review).all()
            for obj in new_query:
                new_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj            
            return new_dict
        else:
            new_query = DBStorage.__session.query(cls).all()
            for obj in new_query:
                new_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj            
            return new_dict
    
    def new(self, obj):
        """Adds new object to db storage"""
        if obj:
            self.__session.add(obj)
    
    def save(self):
        """Saves in dbstorage a object"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete object in databases"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Loads storage dictionary from database"""
        Base.metadata.create_all(DBStorage.__engine)
        session_factory = sessionmaker(bind=DBStorage.__engine,
                                       expire_on_commit=False)
        DBStorage.__session = Session()



        
        
