#!/usr/bin/python3
"""
It’s time to change your storage engine and use SQLAlchemy
"""
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __engine path to the JSON file
        __session: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor of the database """
        config_db = 'mysql+mysqldb://{}:{}@{}:3306/{}'
        password = getenv('HBNB_MYSQL_PWD')
        database = getenv('HBNB_MYSQL_DB')
        user = getenv('HBNB_MYSQL_USER')
        host = getenv('HBNB_MYSQL_HOST')
        hbnb_env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            config_db.format(user, password, host, database),
            pool_pre_ping=True)

        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query of object depending of the class name
         if cls=none query of all type of objects
        """
        my_session = self.__session
        dic = {}

        if instance(cls, str):
            class_print = cls
        else:
            class_print = cls.__name__

        for x in my_session.query(eval(class_print)).all():
            class_type = x.__class__.__name__

            if class_type == class_print:
                dic[class_type + "." + x.id] = x

        return dic

    def new(self, obj):
        """
        Add new obj
        Args:
            obj: given object
        """
        self.__session.add(obj)

    def save(self):
        """
        Save to database
        """
        self.__session.commit()

    def reload(self):
        """
        Create the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def delete(self, obj=None):
        """
        Delete obj from __objects if it’s inside
        """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """
        Close method on the private session attribute on class Session
        """
        self.__session.close()
