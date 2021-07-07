#!/usr/bin/python3
""" Storages """
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {'State': State, 'City': City, 'User': User, 'Place': Place}


class DBStorage:
    """ DB Storage """
    __engine = None
    __session = None

    def __init__(self):
        """ Method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """method all"""
        clsdict = {}
        if cls:
            if cls in classes.keys():
                for i in self.__session.query(classes[cls]).all():
                    key = str(i.__class__.__name__) + "." + str(i.id) #se cambio _ por __
                    clsdict[key] = i
        else:
            for k, v in classes.items():
                for i in self.__session.query(v).all():
                    key = str(i.__class__.__name__) + "." + str(i.id) #se cambio _ por __
                    clsdict[key] = i
        return clsdict

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        ses_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses_fact)
        self.__session = Session()

    def close(self):
        """to end session"""
        self.__session.close()
