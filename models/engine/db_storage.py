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


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):

        username = getenv("HBNB_MYSQL_USER") + ":"
        password = getenv("HBNB_MYSQL_PWD") + "@"
        hostname = getenv("HBNB_MYSQL_HOST") + "/"
        database = getenv("HBNB_MYSQL_DB")
        hbnb_env = getenv("HBNB_ENV")
        dialdriv = "mysql+mysqldb://"
        myengine = dialdriv + username + password
        myengine = myengine + hostname + database
        engine = create_engine(myengine)
        self.__engine = engine

        if hbnb_env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """Returns dict of current database"""
        # fmt: off
        from_databases = {}
        cls_dictionary = {"BaseModel": BaseModel,
                   "User": User, "Place": Place,
                   "State": State, "City": City,
                   "Amenity": Amenity, "Review": Review,}
        # fmt: on
        if cls:
            for key in cls_dictionary.keys():
                if cls.__name__ == key:
                    my_objs = self.__session
                    my_objs = my_objs.query(cls_dictionary[key])
                    my_objs = my_objs.all()
                    obj_cls = key
                    break
            for obj in my_objs:
                object_id = obj.id
                objectkey = "{}.{}".format(obj_cls, object_id)
                from_databases[objectkey] = obj
            return from_databases
        # fmt: off
        queried_classes = (
            self.__session.query(
                City, State, User,
                Place, Review, Amenity)
                .filter(
                    City.state_id == State.id,
                    Place.user_id == User.id,
                    Place.city_id == City.id,
                    Review.place_id == Place.id,
                    Review.user_id == User.id,
                    ).all())
        # fmt: on
        for instances in queried_classes:
            for obj in range(0, len(instances)):
                object_id = instances[obj].id
                # fmt: off
                objectkey = "{}.{}".format(
                    instances[obj].__class__, object_id)
                from_databases.update(
                    {objectkey: instances[obj]})
                # fmt: on
        return from_databases

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
            queried_table = self.__session.query(
                State, City, Place, User).all()
            # fmt: on
            for row in queried_table:
                if obj == row:
                    self.__session.delete(row)
                    break
            self.save()

    def reload(self):
        """Reload, create all tables"""
        Base.metadata.create_all(self.__engine)
        # fmt: off
        factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False)
        # fmt: on
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
