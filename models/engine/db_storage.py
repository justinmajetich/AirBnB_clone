from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, MetaData
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Private class attributes"""
    __engine = None
    __session = None

    def __init__(self):
        """Public instance methods"""
        HBNB_ENV = getenv('HBNB_ENV')
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Public instance method all"""
        dict_new = {}

        if cls:
            query = self.__session.query(cls).all()
            for key, value in query.items():
                dict_new[key] = value
        else:
            for CLS in self.classes:
                query = self.__session.query(CLS).all()
                for key, value in query.items():
                    dict_new[key] = value
        return (dict_new)

    def new(self, obj):
        """Public instance method new"""
        self.__session.add(obj)

    def save(self):
        """Public instante method save"""
        self.__session.commit()

    def delete(self, obj=None):
        """public instance method delete"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Public instance method reload"""
        Base.metadata.create_all(self.__engine)
        session_new = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_new)
