#!/usr/bin/python3

"""
database storage engine
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage():
    """
    database class construct
    """

    __engine = None
    __session = None

    def __init__(self):
        """class constructor"""

        txt = 'mysql+mysqldb://{}:{}@{}:3306/{}'
        environment = os.getenv('HBNB_ENV')
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        storage_type = os.getenv('HBNB_TYPE_STORAGE')

        eng_txt = txt.format(user, password, host, database)
        engine = create_engine(eng_txt, pool_pre_ping=True)
        self.__engine = engine

    def all(self, cls=None):
        """
        method to query database for class name
        """

        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        all_classes = [State, City, Amenity, Review, User, Place]
        dictionary = {}
        session = self.__session
        if cls:
            objs = session.query(cls)
            for each_obj in objs:
                if each_obj:
                    dictionary += each_obj.to_dict()
                    key = each_obj.__class__.__name__ + '.' + each_obj.id
                    value = obj
                    dictionary[key] = value
        else:
            for each_cls in all_classes:
                try:
                    objs = session.query(each_cls)
                except Exception:
                    pass
                for each_obj in objs:
                    if each_obj:
                        key = each_obj.__class__.__name__ + '.' + each_obj.id
                        value = each_obj
                        dictionary[key] = value
        return dictionary

    def new(self, obj):
        """
        add object to current database session
        """

        (self.__session).add(obj)

    def save(self):
        """
        commit all changes to current database session
        """

        (self.__session).commit()

    def delete(self, obj=None):
        """
        delete object from current database session
        """

        if obj:
            (self.__session).delete(obj)

    def reload(self):
        """create tables in the database"""
        from models.base_model import Base
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session()
