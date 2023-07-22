#!/usr/bin/python3
'''db_storage module'''
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
}


class DBStorage:
    '''Representation of dbstorage'''

    __engine = None
    __session = None

    def __init__(self):
        '''Initializes a new instance'''
        u = getenv('HBNB_MYSQL_USER')
        p = getenv('HBNB_MYSQL_PWD')
        h = getenv('HBNB_MYSQL_HOST')
        d = getenv('HBNB_MYSQL_DB')
        c = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(u, p, h, d)

        self.__engine = create_engine(c, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Retrieves all instances of an optional provided class name from the
            current database session'''
        all_objs = {}
        if cls is None:
            for c in classes.values():
                q = self.__session.query(c)
                for o in q:
                    k = o.to_dict()['__class__'] + '.' + o.id
                    if '_sa_instance_state' in o.__dict__:
                        del o.__dict__['_sa_instance_state']
                    all_objs[k] = o
            return all_objs
        cls = eval(cls) if type(cls) is str else cls
        if cls in classes.values():
            q = self.__session.query(cls)
            for o in q:
                k = o.to_dict()['__class__'] + '.' + o.id
                all_objs[k] = o
            return all_objs
        else:
            return None

    def new(self, obj):
        '''Adds an obj to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''Commits all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Deletes the object from the current database session'''
        self.__session.delete(obj)

    def reload(self):
        ''''''
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)

    def close(self):
        '''Removes the current database session'''
        self.__session.close()
