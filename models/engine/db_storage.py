#!/usr/bin/python3
""" module define New engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
import os
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.place import Place
classes = [User, State, City, Amenity, Place, Review]


class DBStorage:
    """
    Intialise Class that represents DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Public instance method"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db),
                pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        with self.session_scope() as session:
            if cls:
                return session.query(cls).all()
            else:
                return session.query(User, State, City, Amenity, Place, Review).all()

    def new(self, obj):
        with self.session_scope() as session:
            session.add(obj)

    def save(self):
        with self.session_scope() as session:
            session.commit()

    def delete(self, obj=None):
        with self.session_scope() as session:
            if obj:
                session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        ss_f = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ss_f)
        self.__session = Session()

    @contextmanager
    def session_scope(self):
        session = self.get_session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_session(self):
        if self.__session is None:
            self.reload()
        return self.__session

    def close(self):
        if self.__session:
            self.__session.close()


