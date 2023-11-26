#!/usr/bin/python3
"""
New engine DBStorage
"""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.user import User
from models.amenity import Amenity

db_user = os.environ['HBNB_MYSQL_USER'] if 'HBNB_MYSQL_USER' in os.environ else None
db_pwd = os.environ['HBNB_MYSQL_PWD'] if 'HBNB_MYSQL_PWD' in os.environ else None
db_host = os.environ['HBNB_MYSQL_HOST'] if 'HBNB_MYSQL_HOST' in os.environ else None
db_name = os.environ['HBNB_MYSQL_DB'] if 'HBNB_MYSQL_DB' in os.environ else None
test = os.environ['HBNB_ENV'] if 'HBNB_ENV' in os.environ else None

class DBStorage:
    """Database engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialisation"""

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(db_user, db_pwd, db_host, db_name),
            pool_pre_ping=True
        )


        if test == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        self.__session = SessionLocal()

    def all(self, cls=None):
        """Returns a dictionary of all objects of the specified class or all classes"""
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for model_class in Base.__subclasses__():
                objects.extend(self.__session.query(model_class).all())

        dictionary = {}
        for obj in objects:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            dictionary[key] = obj

        return dictionary

    def new(self, obj):
        """Adds new object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all models from the database"""
        Base.metadata.create_all(self.__engine)

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        self.__session = SessionLocal()
