from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

from models.base_model import Base
import os

HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_ENV = os.getenv('HBNB_ENV')


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}',
            pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.meta.drop_all(self.__engine)

        self.reload()

    def all(self, cls=None):
        all_objects = {}

        if cls is not None:
            instances = self.__session.query(cls).all()
            for instance in instances:
                all_objects.update({instance.to_dict()['__class__']
                                    + '.' + instance.id: instance})

        else:

            all_cls = [User, Place, State, City, Amenity, Review]

            for _cls in all_cls:
                instances = self.__session.query(_cls).all()
                for instance in instances:
                    all_objects.update({instance.to_dict()['__class__']
                                        + '.' + instance.id: instance})

        return all_objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.query(obj).delete()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()
