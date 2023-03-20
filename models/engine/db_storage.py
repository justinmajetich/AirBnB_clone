#!/usr/bin/python3
"""New engine DbStorage"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

Class_name = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}

class DBStorage:
    """Manage DB storage"""

    __engine = None
    __session = None

    def __init__(self):
        # call value in env
        user = os.getenv("HBNB_MYSQL_USER")
        pswd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        #create engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}}/{}'
        .format(user,
                pswd,
                host,
                db_name),
        pool_pre_ping=True
        )
        # create all table
        Base.metadata.create_all(self.__engine)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session"""
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        dict_objects = {}
        # class given
        if cls != None:
            for obj in self.__session.query(cls).all():
                k = obj.__class__.__name__ + '.' + obj.id
                dict_objects[k] = obj
        else:
            for k, v in Class_name.items():
                cls = v
                for obj in self.__session.query(cls).all():
                k = obj.__class__.__name__ + '.' + obj.id
                dict_objects[k] = obj

        return(dict_objects)
