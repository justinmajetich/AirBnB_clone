#!/usr/bin/env python3
""" Manages database interaction and connectivities
"""
import os
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# CONSTANT
db_cnf = {
 "dialect":"mysql",
 "driver":"mysqldb",
 "env":os.getenv("HBNB_ENV"),
 "host":os.getenv("HBNB_MYSQL_HOST", "localhost"),
 "user":os.getenv("HBNB_MYSQL_USER", "root"),
 "pwd":os.getenv("HBNB_MYSQL_PWD", "root"),
 "db":os.getenv("HBNB_MYSQL_DB","mysql")
}
classes = {	
  "city":City, "state": State, "place":Place,
  "amenity":Amenity, "review":Review, "user":User
}

class DbStorage:
    """ Db engine for database connectivity """
    __engine = None
    __session = None
    def __init__(self):
        """ Constructor exe on instatiation """
        self.__engine = create_engine("{}+{}://{}:{}@{}/{}".format(db_cnf["dialect"], db_cnf["driver"], db_cnf["user"], db_cnf["pwd"], db_cnf["host"], db_cnf["db"]), pool_pre_ping=True, echo=True)
        if db_cnf["env"] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query db for a specific/all domain model """
        _obj = {}
        cls_name = cls().__class__.__name__
        if cls:
            results = self.__session.query(cls).all()
            for obj  in results:
                key = f"{cls_name}.{obj.id}"
                _obj[key] = obj.to_dict()
        else:
            results = []
            for val in classes.values():
                result = self.__session.query(val).all()
                results.extend(result)
            for obj in results:
                key = f"{cls_name}.{obj.id}"
                _obj[key] = obj.to_dict()
        return _obj

    def new(self, obj):
        """ Add new obj to current session """
        self.__session.add(obj)
        print(f"adding {obj} to session")
    def save(self):
        """ Persist all obj in session to db """
        self.__session.commit()
        print("comming to db")
    
    def delete(self, obj=None):
        """ Delete obj from current session """
        self.__session.delete(obj)

    def reload(self):
        """ Reload obj from db to program """
        SessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(SessionFactory)
        Base.metadata.create_all(self.__engine)
