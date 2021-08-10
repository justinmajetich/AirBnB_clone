from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

class DBStorage:
    """Data Base storage"""
    __engine: None
    __session: None
    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database =os.getenv('HBNB_MYSQL_DB')
        environ = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user,password,host, database),
                                    pool_pre_ping=True)
        if environ == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ All classes """
        dct = {}
        if cls is None:
            all_classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']    
            for _cls in all_classes:
                objs = self.__session.query(eval(_cls)())
                for obj in objs:
                    key = obj.__class__.__name + '.' + obj._id
                    dct[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name + '.' + obj._id
                dct[key] = obj
        return (dct)

    def new(self, obj):
        """Add new object"""
        self.__session.add(obj)
    
    def save(self):
        """Confirm the changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete in session if is not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload all tables"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()
