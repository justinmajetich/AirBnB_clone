#!/usr/bin/python3
"""Allows manage storage of hbnb models using SQL Alchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.base_model import BaseModel, Base
from models import user, state, city, amenity, place, review


class DBStorage():
    """Allows manage storage of hbnb models using SQL Alchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine (self.__engine)"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session
        all objects depending of the class name"""
        class_dict = {
            'User': user.User, 'Place': place.Place,
            'State': state.State, 'City': city.City,
            'Amenity': amenity.Amenity, 'Review': review.Review
        }
        query_dict = {}

        if cls:
            if type(cls) == str:
                for obj in self.__session.query(class_dict[cls]).all():
                    query_dict[cls + '.' + obj.id] = obj
            else:
                print(cls)
                for obj in self.__session.query(cls).all():
                    print(obj)
                    query_dict[cls.__name__ + '.' + obj.id] = obj
        else:
            for class_key, class_value in class_dict.items():
                for obj in self.__session.query(class_value).all():
                    query_dict[class_key + '.' + obj.id] = obj

        return query_dict

    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database
        and create the current database session by by using a sessionmaker """
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))

        self.__session = Session()
