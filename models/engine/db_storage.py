#!/usr/bin/python3

"""
Module containing HBnB Console's Database engine
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base

mydb = "mysql+mysqldb"
usr = getenv("HBNB_MYSQL_USER")
pwd = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
db = getenv("HBNB_MYSQL_DB")
environment = getenv("HBNB_ENV")
connect = '{0}://{1}:{2}@{3}:3306/{4}'.format(mydb, usr, pwd, host, db)
db_metadata = MetaData()

class DBStorage:
    """
    Engine for the console's database connection
    Attributes:
        __engine: the DB connection engine
        __session: the current DB session
    """

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(connect, pool_pre_ping=True)
        if environment == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        res = {}
        if cls == 'Amenity':
            query = self.__session.query(Amenity).all()
        elif cls == 'City':
            query = self.__session.query(City).all()
        elif cls == 'Place':
            query = self.__session.query(Place).all()
        elif cls == 'Review':
            query = self.__session.query(Review).all()
        elif cls == 'State':
            query = self.__session.query(State).all()
        elif cls == 'User':
            query = self.__session.query(User).all()
        else:
            query = self.__session.query().all()
        for record in query:
            key = "{}.{}".format(type(record).__name__, record.id)
            value = record.to_dict()
            del value['__class__']
            res.update({key: value})
        return res

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
