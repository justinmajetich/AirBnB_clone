#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    """Defines the database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and links to the MySQL database"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                format(getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects
        depending on class name"""
        session = self.__session
        objects = {}
        if cls:
            for obj in session.query(eval(cls)).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
            
        else:
            for cls in ["User", "State", "City", "Amenity", "Place", "Review"]:
                for obj in session.query(eval(cls)).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

