#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
# from base_model import BaseModel
import os

class DBStorage:
    """Definition of the class"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiation of the class"""
        USER = os.getenv('HBNB_MYSQL_USER')
        PASS = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DB_NAME = os.getenv('HBNB_MYSQL_DB')
        _ENV = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PASS, HOST, DB_NAME), pool_pre_ping=True)

        if _ENV == 'test':
            metadata = MetaData()
            metadata.drop_all(bind=self.__engine)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        def all(self, cls=None):
            """Selection objects, with optional filtering
            by classnames"""
            if cls:
                all_rows = self.__session.query(cls).all()

                #all_cities = session.query(State).order_by(State.id).all()
                fr = all_rows[0]
                cls_name = fr.__dict__['_sa_instance_state'].class_.__name__

                dict_s = {}
                for r in all_rows:
                    del r.__dict__["_sa_instance_state"]
                    dict_s.update({f"{cls}.{r.id}": r.__dict__})

                return dict_s

            else:
                all_rows = self.__session.query(metadata.tables.keys()).all()

            return (all_rows)
