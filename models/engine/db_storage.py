"""Defines the DBStorage engine"""
from os import getenv
import sqlalchemy as db
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class DBStorage:
    '''A class for database storage'''
    __engine = None
    __session = None

    def __init__(self):
        '''creates a database engine'''
        self.__engine = db.create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                           format(getenv("HBNB_MYSQL_USER"),
                                  getenv("HBNB_MYSQL_PWD"),
                                  getenv("HBNB_MYSQL_HOST",
                                  getenv("HBNB_MYSQL_DB"))),
                           pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """query on current database"""
        if cls==None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session(City).all())
            obj.extend(self.__session(User).all())
            obj.extend(self.__session(Place).all())
            obj.extend(self.__session(Review).all())
            obj.extend(self.__session(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            obj = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in obj}

    def new(self, obj):
        '''adds an object to current database'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database session '''
        self.__session.commit()
    
    def delete(self, obj=None):
        '''delete from the current database session obj if not None'''
        self.__session.delete(obj)
    
    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()