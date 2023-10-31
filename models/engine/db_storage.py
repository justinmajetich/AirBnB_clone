#!/usr/bin/python3
# KASPER edited @ 10/30 12:02am
""" database storage engine using SQLAlchemy """
from sqlalchemy import (create_engine, select)
from sqlalchemy import MetaData
from sqlalchemy.orm import (sessionmaker)
import os


class DBStorage:
    """ Database storage engine """

    __engine = None
    __session = None

    def __init__(self):
        un = os.getenv('HBNB_MYSQL_USER')
        pw = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        session_info = f"mysql+mysqldb://{un}:{pw}@{host}/{db}"
        self.__engine = create_engine(session_info, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            md = MetaData()
            md.reflect(self.__engine)
            md.drop_all(self.__engine)

    def all(self, cls=None):
        """ TBC """
        exists = select(cls)
        user_obj = self.__session.scalars(exists).all()
        print(user_obj)
        return user_obj

    def save(self):
        """ TBC """
        self.__session.commit()

    def new(self, obj):
        """ TBC """
        self.__session.add(obj)
        self.save()

    def delete(self, obj=None):
        """ TBC """
        self.__session.delete(obj)

    def reload(self):
        """ TBC """
        from models.base_model import BaseModel, Base
        from models.state import State
        from models.city import City
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
