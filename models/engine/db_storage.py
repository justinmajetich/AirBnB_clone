#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import Base
from sqlalchemy import create_engine
from os import getenv

class DBStorage:
    """Class Docs"""
    __engine = None
    __session = None
    
    def __init__(self):
        """Function Docs"""
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(f'mysql+mysqldb://{hb_user}:{hb_pwd}@{hb_host}/{hb_db}', pool_pre_ping=True)
        
        if hb_env == "test":
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """

        Args:
            cls (_type_, optional): _description_. Defaults to None.
        """
        self.__session = Session(engine)
        for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
            print("{}: {}".format(state.id, state.name))
        self.__session.close()
