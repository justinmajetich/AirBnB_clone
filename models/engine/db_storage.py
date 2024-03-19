#!usr/bin/python3
"""
DBStorage class module
"""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if not cls:
            data = self.__session.query(Amenity)
            data.extend(self.__session.query(City))
            data.extend(self.__session.query(Place))
            data.extend(self.__session.query(Review))
            data.extend(self.__session.query(State))
            data.extend(self.__session.query(User))
        else:
            data = self.__session.query(cls)
        return {obj.__class__.__name__ + '.' + obj.id: obj for obj in data}

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        se_ss = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(se_ss)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
