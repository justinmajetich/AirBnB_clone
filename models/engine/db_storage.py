#!/usr/bin/python3
"""New engine (DataBase)Storage"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import environ
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place, place_amenity
from models.review import Review
from models.base_model import BaseModel, Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(environ.get('HBNB_MYSQL_USER'),
                                              environ.get('HBNB_MYSQL_PWD'),
                                              environ.get('HBNB_MYSQL_HOST'),
                                              environ.get('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True))
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Must return a dictionary like FileStorage"""
        obj_dict = {}
        if cls is None:
            all_objects = (self.__session.query
                           (City, State, User, Place, Review, Amenity)
                           .filter(City.state_id == State.id,
                                   Place.user_id == User.id,
                                   Place.city_id == City.id,
                                   Review.place_id == Place.id,
                                   Review.user_id == User.id,
                                   Amenity.id == place_amenity.amenity_id,
                                   Place.id == place_amenity.place_id)
                           .all())
            for objs in all_objects:
                for obj in range(0, len(objs)):
                    id = objs[obj].id
                    obj_key = '{}.{}'.format(objs[obj].__class__, id)
                    obj_dict.update({obj_key: objs[obj]})
            return obj_dict
        else:
            classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
            }
            for key in classes.keys():
                if cls.__name__ == key:
                    objects = (self.__session.query(classes[key]).all())
                    obj_class = key
                    break
            for obj in objects:
                id = obj.id
                obj_key = '{}.{}'.format(obj_class, id)
                obj_dict.update({obj_key: obj})
            return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        if self.__session is not None:
            self.__session.remove()
