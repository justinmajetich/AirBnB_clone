#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    __engine = None
    __session = None

    user = getenv(HBNB_MYSQL_USER)
    pwd = getenv(HBNB_MYSQL_PWD)
    host = getenv(HBNB_MYSQL_HOST)
    db = getenv(HBNB_MYSQL_DB)


        def __init__(self, *args, **kwargs):
            self.__enigne = create_engine('mysql+mysqldb://{}:{}@lcoalhost:{}/{}'.format(user, pwd, host, db), pool_pre_ping=True)
            if (getenv(HBNB_ENV) == 'test'):
                Base.metadata.dropall()
         def all(self, cls=None):
             dic = {}
             if cls:
                 if type(cls) is str:
                     cls = eval(cls)
                     query = self.__session.query(cls)
                     for elem inquery:
                         key
             
