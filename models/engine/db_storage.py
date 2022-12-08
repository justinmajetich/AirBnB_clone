#!/usr/bin/python3
""""""
from os import environ
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker



class DBStorage:
    """Class DBStorage to get the connection with the database
    Args:
        engine (sqlalchemy.create_engine): engine for sqlalchemy
        sessions (sqlalchemy.orm.sessionmaker): session of the connection"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}' \
                .format(environ.get('HBNB_MYSQL_USER'),
                        environ.get('HBNB_MYSQL_PWD'),
                        environ.get('HBNB_MYSQL_HOST'),
                        environ.get('HBNB_MYSQL_DB')),
                        pool_pre_ping=True)
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """this method must return a dictionary
        Args:
            cls (in classes):
        """
        from models.city import City
        from models.state import State
        classes = {"City": City, "State": State}

        tmp = {}
        if cls is None:
            for clas in classes.values():
                all_cls = self.__session.query(clas).all()
                for obj in all_cls:
                    key = type(obj).__name__ + '.' + obj.id
                    tmp[key] = obj
        else:
            if cls in classes.values():
                all_cls = self.__session.query(cls).all()
                for obj in all_cls:
                    key = type(obj).__name__ + '.' + obj.id
                    tmp[key] = obj
        return (tmp)

    def new(self, obj):
        """add the object to the current database session
        Args:
            obj (): new object to add
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session 
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        Args:
            obj (): obj to delete
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
