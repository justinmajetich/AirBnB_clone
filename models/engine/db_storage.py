#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        from models.base_model import Base
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        mode = os.getenv("HBNB_ENV")
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{password}"
                                      f"@{host}:3306/{db_name}",
                                       pool_pre_ping=True)
        if mode == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        pass

    def new(self, obj):
        pass

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        pass

    def reload(self):
        pass
