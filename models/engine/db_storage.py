#!/usr/bin/python3
"""database storage engine"""
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """class for database storage engine"""
    __engine = None
    __session = None
    dialect = 'mysql'
    driver = 'mysqldb'
    user = os.getenv("HBNB_MYSQL_USER")
    password = os.getenv("HBNB_MYSQL_PWD")
    host = os.getenv("HBNB_MYSQL_HOST")
    database = os.getenv("HBNB_MYSQL_DB")

    def __init__(self):
        """initializes the engine"""
        self.__engine = create_engine(f'{self.dialect}+{self.driver}://\
                                        {self.user}:{self.password}@\
                                        {self.host}/{self.database}',
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)
            self.__session.commit()

    def all(self, cls=None):
        if cls:
            objList = self.__session.query(cls).all()
            listDic = {}
            for obj in objList:
                key = obj.__class__.__name__ + '.' + obj.id
                listDic.update({key: obj})
            return listDic
        else:
            classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
            objList = []
            listDic = {}
            for key in classes.keys():
                objList.append(self.__session.query(key).all())
            for obj in objList:
                key = obj.__class__.__name__ + '.' + obj.id
                listDic.update({key: obj})
            return listDic

    def new(self, obj):
        """adds obj to session"""
        self.__session.add(obj)

    def save(self):
        """saves the current state of session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes the obj from database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """loads a session from database"""
        from sqlalchemy.orm import scoped_session
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
