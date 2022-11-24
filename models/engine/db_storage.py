#!/usr/bin/python3
"""
Module db_storage
"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None
    def __init__(self):
        """Constructor for DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """All function
        all objects depending of the class name
        return a dictionary"""
        classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
        my_dict = {}
        for i in classes:
            if cls is None or cls is classes[i]:
                ob = self.__session.query(classes[i]).all()
                for i in ob:
                    key = "{}.{}".format(type(ob).__name__, ob.id)
                    my_dict[key] = ob
        return my_dict

    def new(self, obj):
        """Add obj to session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes of current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from session if not none"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables in database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        ses = scoped_session(session_factory)
        self.__session = ses()

    def close(self):
        """Close database connection"""
        self.__session.close()
