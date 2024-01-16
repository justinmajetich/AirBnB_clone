#!/usr/bin/python3
'''Database engine'''
import mysqldb
from sqlalchemy import sessionmaker, create_engine, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

HBNB_MYSQL_USER
class DBFileStorage:
    '''Doc later'''
    __engine = None
    __session = None


    def __init__(self):
        """Initiator"""
        connect = 'mysql+mysqldb://{}:{}@{}/{}'
        self.__engine = create_engine(connect.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                        HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)


    def all(self, cls=None):
        """Query all objects from a class (Table)"""

        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            for clss in classes:
                query = self.__session.query(clss).all():
            return query.to_dict()
        else:
            for table_name in Base.metadata.tables.keys():
                if table_name == cls:
                    query = self.__session.query(cls).all()
                    table_todict = query.to_dict()
            return (table_todict)


    def new(self, obj):
        """Add new object to db"""
        self.__session.add(obj)


    def save(self):
        """Commit all changes"""
        self.__session.commit()


    def delete(self, obj=None):
        """Delete an object from the db table"""
        if obj:
            self.__session.delete(obj)
            self.save()


    def reload(self):

        Base.metadata.create_all(self.__engine)
        Session = scoped_seesion(sessionmaker(bind=engine, expire_on_commit=False, scoped_s))
        self.__session = Session()
