#!/usr/bin/python3
"""db storage"""
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity
# from models.place_amenity import PlaceAmenity


class DBStorage:
    __engine = None
    __session = None
    classes = {
        'City': City,
        'State': State,
        'Place': Place,
        'User': User,
        'Review': Review,
        'Amenity': Amenity,
    }

    def __init__(self):
        """innitialize instance"""
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        user = os.getenv('HBNB_MYSQL_USER')
        string = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(user,
                                                           password,
                                                           host,
                                                           database)
        self.__engine = sqlalchemy.create_engine(string, pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """get all objects or objects of certain type"""
        data = {}
        if cls is None or cls.__name__ not in self.classes:
            for i in self.classes.keys():
                queried = self.__session.query(self.classes[i]).all()
                for j in queried:
                    key = j.__class__.__name__ + "." + j.id
                    data[key] = j.to_dict()
        else:
            queried = self.__session.query(cls).all()
            for j in queried:
                key = j.__class__.__name__ + "." + j.id
                data[key] = j.to_dict()
        return data

    def new(self, obj):
        """add a new obj"""
        self.__session.add(obj)

    def save(self):
        """commit to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload db"""
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        session = scoped_session(session_maker)
        self.__session = session()

    def close(self):
        """close session"""
        self.__session.close()
