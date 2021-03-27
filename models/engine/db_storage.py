#!/usr/bin/python3
"""Module for the storage
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage():
    """Class for DB
    """
    __engine, __session = None, None

    def __init__(self):
        """initializer
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )

    def all(self, cls=None):
        """All :D
        """
        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = [State, City, User, Place, Review, Amenity]
        lili = []
        if cls:
            lili = self.__session.query(cls)
        else:
            for cls in classes:
                lili += self.__session.query(cls)
        return {type(c).__name__ + '.' + c.id: c for c in lili}

    def new(self, obj):
        """new
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """save
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reload
        """
        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """close
        """
        self.__session.close()
