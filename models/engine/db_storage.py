#!/usr/bin/python3
"""New engine DBStorage"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy import Column


__engine = None
__session = None

def __init__(self):
    """Engine linked to MySQL database and user"""
    hbnb_dev = hbnb_dev_db
    self.__engine = create_engine(hbnb_dev_db)
