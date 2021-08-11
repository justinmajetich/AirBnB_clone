"""This module defines the sql storage engine"""
# from dotenv import load_dotenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}

# load_dotenv()


class DBStorage:
    """Manages storage of hbnb in mysql db"""
    __engine = None
    __session = None
    objects = {}

    def __init__(self):
        """initializes storage engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user,
                                                 pwd,
                                                 host,
                                                 db),
            pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns all objects depending on the class name"""
        if cls is None and not isinstance(cls, str):
            for key in classes:
                for data in self.__session.query(classes[key]).all():
                    DBStorage.objects[type(
                        data).__name__ + '.' + data.id] = data
        elif cls in classes:
            for data in self.__session.query(classes[cls]):
                DBStorage.objects[type(data).__name__ +
                                  '.' + data.id] = data
        return DBStorage.objects

    def new(self, obj):
        """inserts obj into mysql db"""
        self.__session.add(obj)

    def save(self):
        """commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session"""
        if obj is not None:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """creates all tables in the database and creates current db session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes the session"""
        self.__session.remove()
