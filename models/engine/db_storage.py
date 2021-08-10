#!/usr/bin/python3
"""
    Engine: DBStorage
"""
import os
from models.base_model import Base
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker



class DBStorage():
    """
        DBStorage class to manage database storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            init method to create engine connection
        """
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                                      format(user, passwd, db),
                        pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadat.drop_all(self.__engine)

    def all(self, cls=None):
        """
            query on the current database session
        """
        all_objs = {}

        if cls is not None:
            for row in self.__session.query(eval(cls)).all():
                key = row.__class__.__name__ + '.' + row.id
                all_objs[key] = row
        else:
            classes = ['User', 'State', 'City', 'Amenity', 'Place',
                       'Review']
            for clse in classes:
                for row in self.__session.query(eval(clse)).all():
                    key = row.__class__.__name__ + '.' + row.id
                    all_objs[key] = row
        return all_objs

    def new(self, obj):
        """
            adds object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
            commits all changes of teh current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            delete from the current database session obj != None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
            creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
