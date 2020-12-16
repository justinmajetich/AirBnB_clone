#!/usr/bin/python3
""" DBStorage class """
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage:
    """[DBStorage]"""
    __engine = None
    __session = None

    def __init__(self):
        """__init__"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        environment = os.getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, password, host, database), pool_pre_ping=True)

        if environment == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Return all dbstorage """
        queryClass = [City, State, User, Place, Review]
        queryList_Output = []
        queryDict_Output = {}
        if cls in queryClass:
            queryList_Output = self.__session.query(cls).all()
        else:
            for class_Input in queryClass:
                queryList_Output += self.__session.query(class_Input).all()
        for class_Output in queryList_Output:
            queryDict_Output.update(
                {class_Output.__class__.__name__ + "." + class_Output.id:
                    class_Output})
        return queryDict_Output

    def new(self, obj):
        """ Create a new obj """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commit the changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ Remove an object """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Initializates a session"""
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(self.__engine, expire_on_commit=False)
        ses = scoped_session(Session)
        self.__session = ses()
