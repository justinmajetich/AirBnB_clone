#!/usr/bin/python3
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base

class DBStorage:
    __engine = None
    __session = None
    
    def __init__(self):
        # create the engine
        hbnb_dev = getenv('HBNB_MYSQL_USE')
        hbnb_dev_pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        hbnb_dev_db = getenv('HBNB_MYSQL_DB')
        db_url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(hbnb_dev, hbnb_dev_pwd, host, hbnb_dev_db)
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

def all(self, cls=None):
    pass