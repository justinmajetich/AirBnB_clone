#!/usr/bin/python3

"""
Module containing HBnB Console's Database engine
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from os import environ as env

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
        self.__session = sessionmaker(bind=self.__engine)
        if environment == 'test':
            db_metadata.drop_all()

    def all(self, cls=None):
        res = {}
        if cls is None:
            query = self.__session.query().all()
        else:
            query = self.__session.query(cls).all()
        