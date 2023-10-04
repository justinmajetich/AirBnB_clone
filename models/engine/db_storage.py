'''DBStorage module'''


from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity

from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    '''DBStorage class'''
    __engine = None
    __session = None
    classes = [State, City, User, Place, Review]

    def __init__(self):
        '''instntiate DB object'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        '''return dectinary of all instances of a class'''
        query = []
        dectinary = {}
        if cls:
            query = self.__session.query(eval(cls))
            for column in query:
                key = f"{cls}.{column.id}"
                value = column
                dectinary[key] = value
        else:
            for cls_name in DBStorage.classes:
                query = self.__session.query(cls_name).all()
                for column in query:
                    key = f"{cls_name.__name__}.{column.id}"
                    value = column
                    dectinary[key] = value
        return dectinary

    def new(self, obj):
        '''add a new instence'''
        self.__session.add(obj)

    def save(self):
        '''commit'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete instance'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''reload'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
