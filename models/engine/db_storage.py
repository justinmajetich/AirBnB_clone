#!/usr/bin/python3
"""This module defines the DBStorage class for HBNB project"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and session"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

        """self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST', 'localhost'),
                getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )
        try:
            Base.metadata.create_all(self.__engine)
        except OperationalError as e:
            # pass
            print(e)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)"""

    def all(self, cls=None):
        """Queries all objects depending on the class name"""
        # from models.__classes__ import classes
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

        """from models import classes
        objects = {}

        if cls:
            query_result = self.__session.query(classes[cls]).all()
            objects = {obj.id: obj.to_dict() for obj in query_result}
        else:
            for class_name in classes.values():
                query_result = self.__session.query(class_name).all()
                objects.update({obj.id: obj.to_dict() for obj in query_result})

        return objects"""

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session if obj is not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and sets up the session"""
        # from models.base_model import Base
        # from models.__init__ import classes
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()
        # self.__session = scoped_session(session_factory)()

    def close(self):
        """Closes the current session"""
        self.__session.close()
