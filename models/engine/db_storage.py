#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from os import getenv


class DBStorage(self):
    self.__engine = None
    self.__session = None

    def __init__(self):
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}'
                                      f'@{host}/{database}',
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):

        def new(self, obj):
            return self.__session.add(obj)

        def save(self):
            return self.__session.commit(obj)

        def delete(self, obj=None):
            if obj is not None:
                self.__session.delete(obj)

        def reload(self):
            Base.metadata.create_all(self.__engine)
            Session = scoped_session(sessionmaker(bind=self.__engine,
                                                  expire_on_commit=False))
