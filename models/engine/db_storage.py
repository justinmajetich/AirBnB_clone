#!/usr/bin/env python3

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel


classes = {
          'BaseModel': BaseModel, 'User': User, 'Place': Place,
          'State': State, 'City': City, 'Amenity': Amenity,
          'Review': Review
          }


class db_storage:
    """A method of storage???"""
    __engine = None
    __session = None
    user = getenv('HBNB_MYSQL_USER')
    password = getenv('HBNB_MYSQL_PWD')
    host = getenv('HBNB_MYSQL_HOST')
    database = getenv('HBNB_MYSQL_DB')

    def __init__(self):
        """Instantiation of self"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(
                                          self.user,
                                          self.password,
                                          self.host,
                                          self.database),
                                      pool_pre_ping=True)

        if (self.database == 'hbnb_test_db'):
            cur = self.__engine.cursor()
            cur.execute("DROP TABLES")

    def all(self, cls=None):
        """query current db sesh: all objects of class.name"""
        """if cls=None, query all: User, State, City, etc."""
        tables = {
                  User: 'users', Place: 'places', State: 'states',
                  City: 'cities', Amenity: 'amenities', Review: 'reviews'
                 }
        dict = {}
        for x in classes:
            if cls == x:
                tdsvrbl = self.__session.query(tables[cls])
                for instance in tdsvrbl:
                    dict[cls.__name__ + '.' + instance.id] = instance
                return dict

        else:
            for x in tables:
                womp = self.__session.query(x)
                for y in womp:
                    dict[y.__class__.__name__ + '.' + y.id] = y
            return dict

    def new(self, obj):
        """add object to current db sesh: self.__session"""
        from models import FileStorage
        self.__session.add(obj)

    def save(self):
        """commit all chgs of cur db sesh: self.__session"""
        self.__session.commit

    def delete(self, obj=None):
        """delete from curr db sesh obj: !=None"""
        if obj:
            del obj

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        engine = sessionmaker(bind=self.__engine,
                              expire_on_commit=False)
        Session = scoped_session(engine)
        self.__session = Session()
