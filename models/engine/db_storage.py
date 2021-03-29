#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import session, sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
                                      'mysql+mysqldb://{}:{}@{}/{}'.format(
                                          getenv('HBNB_MYSQL_USER'),
                                          getenv('HBNB_MYSQL_PWD'),
                                          getenv('HBNB_MYSQL_HOST'),
                                          getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True
                                      )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
    	if not obj:
    		c = self.__session.query().filter().all()
    	else:
    		c = self.__session.query(cls).filter.all()
    	for i in c:
    		print(i)
    	return None

    def save(self):
    	self.__session.commit()

    def delete(self, obj=None):
    	if obj:
    		self.__session.delete(obj)

    def reload(self):
    	Base.metadata.create_all(self.__engine)
    	session_factory = sessionmarker(self.__engine,
    					expire_on_commit=False)
    	Session = scoped_session(session_factory)
    	self.__session = Session()
