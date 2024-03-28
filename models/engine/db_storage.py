#!/usr/bin/python3
"""New storage for HBNB Clone V2"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base


class DBStorage:
    """New storage for HBNB Clone V2 via MySQL"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""

        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")

        self.__engine = create_engine('MySQL + MySQL://{}:{}@{}/{}'.
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        self.reload()

    def all(self, cls=None):
        """Return a dictionary"""
        from models import base_model
        from models import user, state, city, amenity, place, review

        classe = {
            'BaseModel': base_model.BaseModel,
            'User': user.User,
            'State': state.State,
            'City': city.City,
            'Amenity': amenity.Amenity,
            'Place': place.Place,
            'Review': review.Review
        }

        type_dict = {}

        if cls is None:
            for classes in classes.values():
                for row in self.__session.query(classe).all():
                    type_dict['{}.{}'.format(
                        classes.__name__, row.id)] = row
        else:
            for row in self.__session.query(cls):
                type_dict['{}.{}'.format(cls.__name__, row.id)] = row

        return type_dict

    def new(self, obj):
        """New method"""
        self.__session.add(obj)

    def save(self):
        """Save method"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete method"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload method"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.session = scoped_session(session_factory)
