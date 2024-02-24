#!/usr/bin/python3

"""
Module containing HBnB Console's Database engine
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from os import environ as env
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base

load_dotenv()

mydb = "mysql+mysqldb"
usr = env["HBNB_MYSQL_USER"]
pwd = env["HBNB_MYSQL_PWD"]
host = env["HBNB_MYSQL_HOST"]
db = env["HBNB_MYSQL_DB"]
environment = env["HBNB_ENV"]
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
        if cls is None:
            query = self.__session.query().all()
        else:
            query = self.__session.query(cls).all()
        for record in query:
            key = "{}.{}".format(record.name, record.id)
            res.update({key: record})

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
        self.__session = scoped_session(session)