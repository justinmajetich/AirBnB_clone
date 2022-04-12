#!/usr/bin/python3
"""
New engine DBStorage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place


class DBstorage():
    __engine = None
    __session = None

    def __init__(self):
