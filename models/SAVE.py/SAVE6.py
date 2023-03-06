#!/usr/bin/python3
from models.base_model import Base, Basemodel
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
        self.__engine =  create_engine('mysql+mysqldb://{}:{}{}/{}'
                           .format(getenv('HBNB_MYSQL_USER'),
                                   getenv('HBNB_MYSQL_PWD'),
                                   getenv('HBNB_MYSQL_HOST'),
                                   getenv('HBNB_MYSQL_DB'), pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.dropall(self.__engine)
    
    def all(self, cls=None):
        cls_pos = ["Review", "City" "State", "Amenity", "User", "Place"]
        ob_lis = []
        if cls is None:
            for item in cls_pos:
                ob_lis.extend(self.__session.query(item).all())
            else:
                if type(cls) == str:
                    cls = eval(cls)
                ob_lis = (self.session.query(cls).all())
                return { "{}.{}".format(type(obj).__name__, obj.id): obj for obj in ob_lis}

    def add(self, obj):
        self.__session.add(obj)

    def sace(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh)
        self.__session = Session()

#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv

storage = FileStorage()
storage.reload()

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
