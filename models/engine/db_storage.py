#!/usr/bin/python3
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker, scoped_session
from os import getenv

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        from models.base_model import Base, BaseModel
        self.__engine =  create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(getenv('HBNB_MYSQL_USER'),
                                   getenv('HBNB_MYSQL_PWD'),
                                   getenv('HBNB_MYSQL_HOST'),
                                   getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.dropall(self.__engine)
    
    def all(self, cls=None):
        cls_list = ["Reviews", "City", "State", "User",
                    "Place", "Amenity"]
        obj_list = []
        if cls is None:
            for cls_name in cls_list:
                obj_list.extend(self.__session.query(cls_name).all())

        else:
            if type(cls) == str:
                cls = eval(cls)
            obj_list = self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__,
                               obj.id): obj for obj in obj_list}

    def add(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh)
        self.__session = Session()

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)