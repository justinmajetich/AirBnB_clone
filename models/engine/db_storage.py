#!/usr/bin/python3
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"Amenity": Amenity, "City": City, "Place": Place,
            "Review": Review, "State": State, "User": User}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        db_user = environ.get('HBNB_MYSQL_USER')
        db_pwd = environ.get('HBNB_MYSQL_PWD')
        db_host = environ.get('HBNB_MYSQL_HOST')
        db_name = environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                db_user, db_pwd, db_host, db_name),
            pool_pre_ping=True
        )

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        session = self.__session

        if cls:
            objects = session.query(cls).all()
        else:
            objects = []
            for cls in classes:
                objects.extend(session.query(cls).all())

        return {'{}.{}'.format(type(obj).__name__, obj.id): obj for obj in objects}

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    @property
    def session(self):
        return self.__session
