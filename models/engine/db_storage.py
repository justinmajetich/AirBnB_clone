#!usr/bin/python3
"""
Module documentation
"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
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

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(user, password, host, database), pool_pre_ping=True)

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

                objs =  self.__session.query(cls)

            return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs}

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()


    def delete(self, obj=None):
        if obj is not None:
                self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session()
