from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv


classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = 'localhost'
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        print(HBNB_MYSQL_USER)
        print(HBNB_MYSQL_PWD)

        print(HBNB_MYSQL_HOST)

        print(HBNB_MYSQL_DB)

        print(HBNB_ENV)

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
            pool_pre_ping=True
        )
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        all_objects = {}
        if cls is not None:
            print(type(cls))
            if isinstance(cls, str):
                cls_s = eval(cls)
            else:
                cls_s = cls
            select = self.__session.query(cls_s)
        else:
            select = self.__session.query().all()
        objects = select.all()
        for objct in objects:
                all_objects["{}.{}"
                            .format(
                                objct.__class__.__name__, objct.id
                                )] = objct
        return all_objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
