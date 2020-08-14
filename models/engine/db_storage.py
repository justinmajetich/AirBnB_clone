#!/usr/bin/python3
""" db storage """

from os import getenv
from models.base_model import Base, BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine


class DBStorage():
    """ db storage """

    __engine = None
    __session = None

    def __init__(self):
        ''' init '''

        db_user = getenv('HBNB_MYSQL_USER')
        db_pass = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                      db_user, db_pass, db_host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        ''' reload '''
        from sqlalchemy.orm import sessionmaker as sm, scoped_session

        Base.metadata.create_all(self.__engine)
        sess = sm(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def all(self, cls=None):
        ''' all '''

        if cls is None:
            objects = self.__session.query(State).all()
            objects += self.__session.query(City).all()
            objects += self.__session.query(User).all()
            objects += self.__session.query(Place).all()
            """
            objects += self.__session.query(Amenity).all()
            objects += self.__session.query(Review).all()
            """
        else:
            objects = self.__session.query(cls)

        ret = {}
        for obj in objects:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            ret[key] = obj

        return ret

    def new(self, obj):
        ''' new '''

        if obj is None:
            return
        self.__session.add(obj)

    def save(self):
        ''' save '''

        self.__session.commit()

    def delete(self, obj=None):
        ''' delete '''

        if obj is None:
            return
        else:
            self.__session.delete(obj)
