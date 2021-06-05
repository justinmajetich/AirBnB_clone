#!/usr/bin/env python3

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class db_storage:
    """A method of storage???"""
    __engine = None
    __session = None
    user = getenv('HBNB_MYSQL_USER')
    password = getenv('HBNB_MYSQL_PWD')
    host = getenv('HBNB_MYSQL_HOST')
    database = getenv('HBNB_MYSQL_DB')

    def __init__(self):
        """Instantiation of self"""
        self.__engine =  create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                        .format(
                                        self.user, 
                                        self.password, 
                                        self.database), 
                                        pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        tediousvariable = self.__session.query()

        if (self.database == 'hbnb_test_db'):
            cur = self.__engine.cursor()
            cur.execute("DROP TABLES")

    def all(self, cls=None):


query on the current database session (self.__session) all objects depending of the class name (argument cls)
if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
this method must return a dictionary: (like FileStorage)
key = <class-name>.<object-id>
value = object
new(self, obj): add the object to the current database session (self.__session)
save(self): commit all changes of the current database session (self.__session)
delete(self, obj=None): delete from the current database session obj if not None
reload(self):
create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine))
create the current database session (self.__session) from the engine (self.__engine) by using a sessionmaker - the option expire_on_commit must be set to False ; and scoped_session - to make sure your Session is thread-safe
