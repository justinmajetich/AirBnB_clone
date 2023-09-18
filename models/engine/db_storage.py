#!/usr/bin/python3
"""a script for DB Storage Engine"""
import os
from sqlalchemy import Base
from sqlalchemy import create_engine


class DBStorage():
    """create the engine to be linked to the MySQL
    database
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of engine"""

        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv("HBNB_ENV")

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, database)

        engine = create_engine(db_url, pool_pre_ping=True)
        self.__engine = engine
        if env == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """query on the current database session
        (self.__session) all objects depending of the class
        name (cls)"""
        obj_list = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        objects = []

        if cls is not None:
            objects.extend(self.__session.query(cls).all())  # objects
        else:
            for item in obj_list:
                objects.extend(self.__session.query(item).all())

        dict = {}
        for obj in objects:
            k = f"{obj.__class__.__name__}.{obj.id}"
            dict[k] = obj

        return dict
