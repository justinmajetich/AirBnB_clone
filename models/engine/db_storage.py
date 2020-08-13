import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }


class DBStorage:
    """Comment but im lazy"""
    __engine = None
    ___session = None

    def __init__(self):
        """Init"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                    format(HBNB_MYSQL_USER,
                                           HBNB_MYSQL_PWD,
                                           HBNB_MYSQL_HOST,
                                           HBNB_MYSQL_DB,
                                           HBNB_ENV))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            dictio = {}
            for key, val in self.__objects.items():
                if cls == val.__class__ or cls == val.__class__.__name__:
                    dictio[key] = val
            return dictio
        return FileStorage.__objects

    def new(self, obj):
        """COMMENT"""
        self.___session.add(obj)

    def save(self):
        """COMMENT"""
        self.___session.commit()

    def delete(self, obj=None):
        """COMMENT"""
        if obj is not None:
            self.___session.delete(obj)

    def reload(self):
        """sadsdasd """
        Base.metadata.create_all(self.__engine)
        sessionf = sessionmaker(bind=self.__engine, expire_on_commit=(False))
        Session = scoped_session(sessionf)
        self.session = Session

    def close(self):
        """tasdasd"""
        self.___session.remove()
