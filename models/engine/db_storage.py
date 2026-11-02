#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.state import State
from models.city import City

from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """this is the constructor"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")  # (here = localhost)
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, password, host, database, pool_pre_ping=True))

        if (env == "test"):
            # drop_all(engine)
            Base.metadata.drop_all(self.__engine)

            # User.__table__.drop()
            # Session = sessionmaker(bind=self.__engine)
            # session = Session()
            # drop = session.

    def all(self, cls=None):
        """ Query on the current database session all objects """

        objDict = {}
        if cls is None:
            classes = {
                'State': State,
                'City': City,
                'User': User,
                'Place': Place,
                'Review': Review,
                'Amenity': Amenity}
            for key, value in classes.items():
                # print("Here")
                objct = self.__session.query(value).all()
                for obj in objct:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    # print(key)
                    objDict[key] = obj
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objct = self.__session.query(cls)
            for obj in objct:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objDict[key] = obj

        # print(objDict)
        return objDict

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if (obj):
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """method calls remove method on private session attr"""
        self.__session.close()
