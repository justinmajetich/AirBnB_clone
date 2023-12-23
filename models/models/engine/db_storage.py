#!/usr/bin/python3
"""

"""
# handles the details of how to connect to the database and execute SQL commands
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.exc import InvalidRequestError
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
    
    """
    __engine = None
    __session = None
    def __init__(self) -> None:
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database_name = getenv("HBNB_MYSQL_DB")
        database_url = "mysql+mysqldb://{}:{}@{}/{}".format(username,
                                                            password,
                                                            host,
                                                            database_name)
        self.__engine = create_engine(database_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        
        """
        objs_list = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                objs_list = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                objs_list.extend(self.__session.query(subclass).all())
        obj_dict = {}
        for obj in objs_list:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict
    
    def new(self, obj):
        """
        
        """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """"
        
        """
        self.__session.commit()    

                
    def delete(self, obj=None):
        """
        
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        
        """
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
