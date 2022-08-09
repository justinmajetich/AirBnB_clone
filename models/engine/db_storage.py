#!/usr/bin/python3
""" new engine DBStorage"""
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """new engine DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host,
                                              database), pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session
        all objects depending of the class name
        if cls=None
        query all types of objects"""
        db_dict = {}
        objects_list = {User, State, City, Amenity, Place, Review}
        if cls is not None:
            for cls in objects_list:
                result = self.__session.query(cls).all()
                for obj in result:
                    key = obj.__class__.__name__ + '.' + obj.id
                    db_dict[key] = obj
        return db_dict

    """
    if cls is None:
        for obj in self.__session.query(User, State, City, Amenity, Place, Review).all():
            key = obj.__class__.__name__ + '.' + obj.id
            db_dict[key] = obj
    else:
        for obj in self.__session.query(cls).all():
            key = obj.cls.__name__ + '.' + obj.id
            db_dict[key] = obj
    return db_dict
    """


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
        """create all tables in the database
        create the current database session from engine"""
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
