#!/usr/bin/python3
"""This module manage database connection and Queries"""
import os
from sqlalchemy import create_engine


class DBStorage:
    """This class manages storage of hbnb models in Database"""
    # TODO add class attributes
    __engine = None
    __session = None

    def __init__(self):
        """Initializer"""
        from models.base_model import Base
        # TODO create an engine with env_var
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(
                                         os.getenv("HBNB_MYSQL_USER"),
                                         os.getenv("HBNB_MYSQL_PWD"),
                                         os.getenv("HBNB_MYSQL_HOST"),
                                         os.getenv("HBNB_MYSQL_DB"),
                                         pool_pre_ping=True
                                         )
                                      )
        # TODO drop all tables in test environnment
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    # TODO create all method for querying db
    def all(self, cls=None):
        """Querying all objects"""
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        from models.user import User
        rows = []
        if cls:
            rows = self.__session.query(cls)
        else:
            rows += self.__session.query(State)
            rows += self.__session.query(City)
            rows += self.__session.query(Place)
            rows += self.__session.query(Amenity)
            rows += self.__session.query(Review)
            rows += self.__session.query(User)
        return {row.__class__.__name__ + '.' + row.id: row for row in rows}

    # TODO create new method add a in current session db
    def new(self, obj):
        """Add a new object to current session database"""
        self.__session.add(obj)

    # TODO create save methon commit changes to current session db
    def save(self):
        """Commits changes to the current session database"""
        self.__session.commit()

    # TODO create delete method deletes from the current session db
    def delete(self, obj=None):
        """Deletes from the current session database"""
        if obj:
            self.__session.delete(obj)

    # TODO create reload methon to reload engine instance
    def reload(self):
        """Reloads current session instance"""
        from sqlalchemy.orm import sessionmaker, scoped_session
        from models.base_model import Base
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        )
        self.__session = Session()

    def close(self):
        """Close session"""
        self.__session.close()
