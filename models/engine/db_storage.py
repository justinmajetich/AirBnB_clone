#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        self.user = getenv("HBNB_MYSQL_USER", default=None)
        self.passwd = getenv("HBNB_MYSQL_PWD", default=None)
        self.db = getenv("HBNB_MYSQL_DB", default=None)
        self.host = getenv("HBNB_MYSQL_HOST", default=None)
        self.url = f"mysql+mysqldb://{self.user}:{self.passwd}@{self.host}/{self.db}"
        self.__engine = create_engine(self.url, pool_pre_ping=True)
        if getenv("HBNB_ENV", default=None) == "test":
            # Drop all tables
            Base.metadata.drop_all(bind=DBStorage.__engine)

    def all(self, cls=None):
        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}
        # obj = {}
        if cls in classes:
            cls_objects  = self.__session.query(classes[cls]).all()
            for co in cls_objects:
                print(co.id)
        if cls == None:
            for key, val in classes.items():
                print(self.__session.query(val).all())

    def new(self, obj):
        if obj is not None:
            self.__session.add(obj)
    def save(self):
        self.__session.commit()
    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
    def reload(self):
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False, )
        Session = scoped_session(session_factory)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)


        


