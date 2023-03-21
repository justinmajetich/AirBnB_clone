#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
""" DOC """


class DBStorage:
    """ DOC """
    __engine = None
    __session = None

    def __init__(self, engine=None, session=None):
        """ DOC """
        from models.city import City
        from models.state import State
        from models.base_model import BaseModel, Base

        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        database = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")
        self.__engine = create_engine(f"mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost:3306/hbnb_dev_db", pool_pre_ping=True)
        
        Session = sessionmaker(bind=self.__engine)
        Session.configure(bind=self.__engine)
        self.__session = Session()

        if env == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)


    def all(self, cls=None): 
        """ query on the current database session """
        #from models.user import User
        #from models.place import Place
        from models.state import State
        from models.city import City
        #from models.amenity import Amenity
        #from models.review import Review

        Session = sessionmaker(bind=self.__engine)
        session = Session()

        dic = {}
        if cls is None:
            self.__session = session.query(State).join(City).all()
            for obj in self.__session:
                dic[f"{obj.name}.{obj.id}"] = obj
        else:
            self.__session = session.query(cls.__name__).all()
            #dic
        #for obj in self.__session:
        return dic
        
    def new(self, obj):
        """ add the object to the current database session """
        session.add(obj)
    
    def save(self):
        """ commit all changes of the current database session """
        session.commit()
        
    def delete(self, obj=None):
        """ delete from the current database session obj if not None """

        if obj is None:
            return
        else:
            session.delete(obj)

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy) """
        from sqlalchemy.ext.declarative import declarative_base
        from models.city import City
        from models.state import State
        
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(self.__session)
