#!/usr/bin/python3
"""class file DBStorage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage():
    """the DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        """initiate a dbstorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True
        ))

        if getenv("HBNB_ENV") == "test":
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """retrives all objects of a class name"""
        from models.base_model import Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.state import State
        new_dict = {}
        all_class = [City, State, User, Place, Review, Amenity]
        list_objects = []
        if cls is None:
            for i in range(len(all_class)):
                list_objects += self.__session.query(all_class[i]).all()
        else:
            list_objects += self.__session.query(cls).all()

        for element in list_objects:
            key = "{}.{}".format(element.__class__.__name__, element.id)
            new_dict[key] = element
        return new_dict

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and the current
           database session"""
        from models.base_model import Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.state import State
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close method: close or remove the session"""
        self.__session.close()
