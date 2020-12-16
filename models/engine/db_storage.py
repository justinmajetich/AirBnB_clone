#!/usr/bin/python3
""" Storages """
from models.base_model import BaseModel, Base
from models.state import state
from sqlalchemy import Column, String, ForeignKey, DateTime
from models.city import city
from os import getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """ DB Storage """
    __engine = None
    __session = None

    def __init__(self):
        """ Method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                            getenv('HBNB_MYSQL_USER'),
                            getenv('HBNB_MYSQL_PWD'),
                            getenv('HBNB_MYSQL_HOST'),
                            getenv('HBNB_MYSQL_DB')),
                            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        querys_dic = {}
        if cls is not None:
            i_query = self.__session.query(eval(cls)).all()
        else:
            i_query = self.__session.query(User).all()
            i_query += self.__session.query(State).all()
            i_query += self.__session.query(City).all()
            i_query += self.__session.query(Amenity).all()
            i_query += self.__session.query(Place).all()
            i_query += self.__session.query(Review).all()
        for item in i_query:
            key = '{}.{}'.format(type(item).__name__, item.id)
            querys_dic[item] = key
        return querys_dic

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        ses_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses_fact)
        self.__session = Session()

    def close(self):
        """to end session"""
        self.__session.close()
