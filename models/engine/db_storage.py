#!/usr/bin/python3
""" """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage():
    """DBStorage Class"""
    __engine = None
    __session = None
    user = getenv('HBNB_MYSQL_USER') 
    pwd = getenv('HBNB_MYSQL_PWD')
    host = getenv('HBNB_MYSQL_HOST')
    db = getenv('HBNB_MYSQL_DB')
    environment = getenv('HBNB_ENV')
    url_eng = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
    
    def __init__(self):
        """ """
        self.__engine = create_engine(url_eng, pool_pre_ping=True)
        if environment == 'test':
            metadata.drop_all(bind=self.__engine)
    
    del all(self, cls=None):
        """ """
        pass
