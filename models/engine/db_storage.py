#!/usr/bin/python3
"""Script defnes DataBAse storage class"""

from sqlalchemy import create_engine, MetaData
from os import environ
from models.base_model import Base

class DBStorage:
    """database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes instance varibles/attributes"""
        user = environ['HBNB_MYSQL_USER']
        pwrd = environ['HBNB_MYSQL_PWD']
        host = environ['HBNB_MYSQL_HOST']
        db = environ['HBNB_MYSQL_DB']
        is_test = environ['HBNB_ENV']
        _url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwrd, host, db)
        self.__engine = create_engine(_url, pool_pre_ping=True)

        if is_test == 'test':
            metadata = MetaData()
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        from sqlalchemy.orm import Session
        from models.user import User
        from models.state import State
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        from sqlalchemy.orm import class_mapper


        if not self.__session:
            self.__session = Session(self.__engine)
        if cls:
            all_objs = self.__session.query(cls).all()
        else:
            all_objs = []
            model_list = [State, City]
            for model in model_list:
                all_objs.extend(self.__session.query(class_mapper(model)).all())

        obj_dict = {}
        for obj in all_objs:
            key = obj.__name__ + '.' + obj.id
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        from models.user import User
        from models.state import State
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        from sqlalchemy.orm import sessionmaker, scoped_session

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)




        
