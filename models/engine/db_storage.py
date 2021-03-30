#!/usr/bin/python3
import models
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        # if getenv("HBNB_ENV") == "test":
        Base.metadata.drop_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        allClasses = ["State", "Place", "User", "Amenity", "Review", "City"]
        listClasses = []
        dictClasses = {}
        if cls is not None and cls.__class__.__name__ in allClasses:
            print("if*" * 10)
            listClasses = self.__session.query(State).all()
        else:
            print("else*" * 10)
            # for cls in allClasses:
            listClasses = self.__session.query(State).all()
            print(listClasses, "List of classes")
        for classObject in listClasses:
            key = classObject.__class__.__name__ + "." + classObject.id
            dictClasses[key] = classObject
        print(dictClasses, "dict of classes")
        return dictClasses

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
