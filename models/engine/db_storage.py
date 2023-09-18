#!/usr/bin/python3
"""
    This is the Database engine
    Author: Peter Ekwere
"""
from sqlalchemy import create_engine, MetaData
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place

class DBStorage:
    """ This Class will handle all data base storage """

    __engine = None
    __session = None
    
    environment = os.environ.get("HBNB_ENV")
    user = os.environ.get("HBNB_MYSQL_USER")
    password = os.environ.get("HBNB_MYSQL_PWD")
    my_host = os.environ.get("HBNB_MYSQL_HOST")
    database = os.environ.get("HBNB_MYSQL_DB")

    def __init__(self):
        """ This is the DBStorage constructor """
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(DBStorage.user, DBStorage.password,
                    DBStorage.my_host, DBStorage.database), pool_pre_ping=True
                )
        if DBStorage.environment == "test":
            metadata = MetaData(bind=self.__engine)
            test_table = Table(database, metadata, autoload=True)
            test_table.drop()

    def all(self, cls=None):
        """ This Method returns all objects based on class """
        dictionary = {}
        if cls == None:
            class_list = [User, State, City, Amenity, Place]
            for a_class in class_list:
                all_instance = self.__session.query(a_class)
                for instance in all_instance:
                    key = f"{instance.name}.{instance.id}"
                    dictionary[key] = instance
        else:
            all_instance = self.__session.query(cls)
            for instance in all_instance:
                key = f"{instance.name}.{instance.id}"
                dictionary[key] = instance

        return dictionary

    def new(self, obj):
        """ This Method adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
       """ This Method commit all changes of the current database session """
       self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not Non"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create's all tables in the database and create's the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
