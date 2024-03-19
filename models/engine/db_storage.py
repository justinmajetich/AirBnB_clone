#!/usr/bin/python3
"""Engine for database"""


from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# icecrean debbuger (comment after use)
# from icecream import ic


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        dialdriv = getenv("DIALECT_DRIVER") + "://"
        username = getenv("HBNB_MYSQL_USER") + ":"
        password = getenv("HBNB_MYSQL_PWD") + "@"
        hostname = getenv("HBNB_MYSQL_HOST") + "/"
        database = getenv("HBNB_MYSQL_DB")
        hbnb_env = getenv("HBNB_ENV")
        myengine = dialdriv + username + password
        myengine = myengine + hostname + database
        engine = create_engine(myengine)
        self.__engine = engine

        if hbnb_env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """Returns dict of current database"""
        dictionary_from_database = {}
        # fmt: off
        dictionary_from_classes_ = {
            "BaseModel": BaseModel,
            "User": User, "Place": Place,
            "State": State, "City": City,
            "Amenity": Amenity, "Review": Review,
        }
        # fmt: on

        if cls:
            for key in dictionary_from_classes_.keys():
                if cls.__name__ == key:
                    # fmt: off
                    my_objs = self.__session.query(
                        dictionary_from_classes_[key]).all()
                    # fmt: on
                    obj_cls = key
                    break

            for instance in my_objs:
                instance_id_ = instance.id
                instance_key = "{}.{}".format(obj_cls, instance_id_)
                dictionary_from_database[instance_key] = instance
            return dictionary_from_database

        # fmt: off
        all_objects = (
            self.__session.query(
                City, State, User, Place, Review, Amenity
                ).filter(City.state_id == State.id,
                         Place.user_id == User.id,
                         Place.city_id == City.id,
                         Review.place_id == Place.id,
                         Review.user_id == User.id,).all())
        # fmt: on

        for my_object in all_objects:
            for instance in range(0, len(my_object)):
                instance_id_ = my_object[instance].id
                # fmt: off
                instance_key = "{}.{}".format(
                    my_object[instance].__class__, instance_id_)
                dictionary_from_database.update(
                    {instance_key: my_object[instance]})
                # fmt: on
        return dictionary_from_database

    def new(self, obj):
        """Add new obj"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """Save and commit session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj"""
        if obj is not None:
            # fmt: off
            results = self.__session.query(
                State, City, Place, User).all()
            # fmt: on
            for row in results:
                if obj == row:
                    self.__session.delete(row)
                    break
            self.save()

    def reload(self):
        """Reload, create all tables"""
        Base.metadata.create_all(self.__engine)
        # fmt: off
        factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        # fmt: on
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
