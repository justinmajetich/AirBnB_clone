#!/usr/bin/python3
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
""" DOC """


class DBStorage:
    """ DOC """
    __engine = None
    __session = None

    def __init__(self):
        """ DOC """
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        database = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{database}", pool_pre_ping=True)
        #self.__engine = create_engine(f"mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost:3306/hbnb_dev_db", pool_pre_ping=True)

        Session = sessionmaker(bind=self.__engine)
        Session.configure(bind=self.__engine)
        self.__session = Session()
        
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None): 
        """ query on the current database session """
        dic = {}
        if cls is None:
            q = self.__session.query(State).all()
            q = self.__session.query(City).all()
            q = self.__session.query(Place).all()
            q = self.__session.query(Review).all()
            q = self.__session.query(User).all()
        else:
            q = self.__session.query(cls).all()
        for obj in q:
            dic[f"{obj.name}.{obj.id}"] = obj
        return dic
        
    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)
    
    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()
        
    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is None:
            return
        else:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy) """ 
        Base.metadata.create_all(self.__engine)   
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(s)
        
