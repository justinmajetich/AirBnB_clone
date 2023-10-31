#!/usr/bin/python3
"""Engine for SQL Database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ


class DBStorage():
    """Class for storage of models in db"""
    __engine = None
    __session = None

    def __init__(self):
        """Initilization of db storage engine"""
        self.__engine = create_engine('mysql+mysqldb://' +
                                      environ.get('HBNB_MYSQL_USER') + ':' +
                                      environ.get('HBNB_MYSQL_PWD') + '@' +
                                      environ.get('HBNB_MYSQL_HOST') + '/' +
                                      environ.get('HBNB_MYSQL_DB'),
                                      pool_pre_ping=True)
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """retrurns all of a class, or all"""
        from models.base_model import BaseModel
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        session = self.__session()
        objects = {}
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            if cls in classes:
                objects = session.query(cls).all()
        else:
            for cls in classes:
                objects.update({obj.__class__.__name__ + '.' + obj.id: obj
                                for obj in session.query(cls).all()})
        session.close()
        return objects

    def new(self, obj):
        """adds new object to db"""
        self.__session.add(obj)

    def save(self):
        """saves session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create session"""
        from models.base_model import BaseModel
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
