#!/usr/bin/python3
"""DB_storage engine"""
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage():
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of DBStorage class"""
        usr = getenv('HBNB_MSYQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        hst = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        envy = getenv('HBNB_ENV')
        adr = "mysql+mysqldb://{}:{}@{}/{}".format(usr, pwd, hst, db)
        self.__engine = create_engine(adr, pool_pre_ping=True)
        if envy == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current db session all objects depending on class name"""
        obl = {}
        for x in classes:
            if cls is None or cls is x or cls is classes[x]:
                objs = self.__session.query(classes[x]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    obl[key] = obj
        return (obl)

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.query(obj).delete()

    def reload(self):
        """Create all tables in the DB. Create current DB session
        from the engine by using a sessionmaker."""
        Base.metadata.create_all(self.__engine)
        sessy = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessy)
        self.__session = Session
