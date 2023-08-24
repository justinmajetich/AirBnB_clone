from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv


USER = getenv('HBNB_MYSQL_USER')
PASSWORD = getenv('HBNB_MYSQL_PWD')
HOST = getenv('HBNB_MYSQL_HOST')
DATABASE = getenv('HBNB_MYSQL_DB')
Base = declarative_base()


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            USER, PASSWORD, HOST, DATABASE), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        """"Query on the current database session all objects depending
        of the class name 'cls', if cls is none is then all classes"""
        from models import User
        from models import State
        from models import City
        from models import Amenity
        from models import Place
        from models import Review
        from models import BaseModel
        cls_dict = {}
        if cls is None:
            cls = (User, State, City, Amenity, Place, Review)
        for a_cls in cls:
            objs = self.__session.query(a_cls).all()
            for obj in objs:
                key = '{}.{}'.format(a_cls, obj.id)
                cls_dict[key] = obj
        return cls_dict

    def new(self, obj):
        """Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in the database if not exists """
        from models import BaseModel
        from models import User
        from models import State
        from models import City
        from models import Amenity
        from models import Place
        from models import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
