#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone""" #Nuevo Revisar archivo
import os
# SE SETEAN AQUI?
os.environ[HBNB_ENV] = "dev" # drop all tables if the environment variable HBNB_ENV is equal to test
os.environ[HBNB_MYSQL_USER] = "hbnb_dev"
os.environ[HBNB_MYSQL_PWD] = ""
os.environ[HBNB_MYSQL_HOST] = "localhost"
os.environ[HBNB_MYSQL_DB] = "hbnb_dev_db"
os.environ[HBNB_TYPE_STORAGE] = "db"


class DBStorage:
    """This class manages storage of hbnb models in DB format"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format( #REVISAR COMO SE HACE EL GET DE VARIABLES DE AMBIENTE
                                        getenv(HBNB_MYSQL_USER), getenv(HBNB_MYSQL_PWD), getenv(HBNB_MYSQL_HOST), getenv(HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
    
    def all(self, cls=None):
        Base.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)
        classdb_dict = {}
        if cls is None:
           query_list = self.__session.query(User, State, City, Amenity, Place, Review).all()
           for item in query_list:
            classdb_dict[item.__class__.__name__ + "." + item.id] = item #REVISAR SI FUNCIONA
        else:
            query_list = session.query(cls)
            for item in query_list:
                classdb_dict[cls + "." + item.id] = item
        return classdb_dict

    def new(self, obj):
        Base.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)
        self.__session.add(obj) #REVISAR
    
    def save(self):
        Base.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)
        self.__session.commit()
    
    def delete(self, obj=None):
        Base.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)
        if obj not None:
            self.__session.delete(obj)
    
    
    
