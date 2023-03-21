#!usr/bin/python3
"""
Module documentation
"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes_list = [User, Place, State, City, Amenity, Review]

class DBStorage:
    """
    Class's documentation
    """
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}', pool_pre_ping=True)

        if (env == "test"):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        if cls is None:
            with self.__session() as session:
                objs = session.query(classes_list[0]).all()
                for i in range(1, len(classes_list)):
                    objs.extend(session.query(classes_list[i].all()))
        else:
            if isinstance(cls, str):
                cls = eval(cls)

            with self.__session() as session:
                objs =  session.query(cls)

            return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs}

    def new(self, obj):
        with self.__session() as session:
            session.add(obj)

    def save(self):
        with self.__session() as session:
            session.commit()

    def delete(self, obj=None):
        if obj is not None:
            with self.__session() as session:
                session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)
