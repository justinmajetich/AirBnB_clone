#!/usr/bin/python3
"""defines the DB storage module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    """a DB storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """public instance method"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'
                .format(
                    getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')
                    ),
                pool_pre_ping=True
                )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects of class name"""
        objs = {}
        classes = {
                'BaseModel': BaseModel
                }
        if cls:
            query = self.__session.query(classes[cls])
            for obj in query.all():
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objs[key] = obj
        else:
            for name, cls in classes.items():
                query = self.__session.query(cls)
                for obj in query.all():
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objs[key] = obj
        return objs

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()
