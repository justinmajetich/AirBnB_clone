#!/usr/bin/python3
'''Storage engine for MySQL database'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from environ import get_env
from models.base_model import Base


class DBStorage:
    '''A database storage engine'''

    __engine = None
    __session = None


    def __init__(self) -> None:
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            get_env('HBNB_MYSQL_USER'),
            get_env('HBNB_MYSQL_PWD'),
            get_env('HBNB_MYSQL_HOST'),
            get_env('HBNB_MYSQL_DB')
        ), pool_pre_ping=True)

        if get_env('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''queries the database session depending on ``cls``'''
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        __models = [User, State, City, Amenity, Place, Review]

        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(*__models)
        
        return {f'{obj.__class__.__name__}.{obj.id}': obj 
            for obj in objs
        }
        
    def new(self, obj):
        '''adds a new obj to database'''
        self.__session.add(obj)

    def save(self):
        '''commits all changes to database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''deletes obj from session'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''reloads all database and create the session'''
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)
