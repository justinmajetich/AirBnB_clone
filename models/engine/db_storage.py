from sqlalchemy import create_engine
from sqlalchemy import metadata
from sqlalchemy.orm import sessionmaker
import os
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ DB_Storage """
    __engine = None
    __session = None

    def __init__(self):

        """init 
        user is the SQL User
        Password is the SQL Password
        host is the host
        db is the database
        """

        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, password, host, db),
                                      pool_pre_ping=True
    
     Base.metadata.create_all(self.__engine)
     if os.getenv("HBNB_ENV") = test:
        Base.metadata.drop_all(self.__engine)

        def new(self, obj):
            """ add the object to the current database session"""
            self.__session.add(obj)
        
        def save(self):
            """ commit all changes of the current database session """
            self.__session.save()
        
        def delete(self, obj=None):
            """ delete from the current database session """
            self.__session.delete(obj)

        


