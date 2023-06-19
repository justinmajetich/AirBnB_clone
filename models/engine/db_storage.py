from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base_model import Base
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
         # Retrieve MySQL configuration from environment variables
        mysql_user = os.environ.get('HBNB_MYSQL_USER')
        mysql_password = os.environ.get('HBNB_MYSQL_PWD')
        mysql_host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
        mysql_database = os.environ.get('HBNB_MYSQL_DB')

        # Create the engine
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(mysql_user, mysql_password, mysql_host, mysql_database),
            pool_pre_ping=True)

        # Drop all tables if HBNB_ENV is 'test'
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Create all tables
        Base.metadata.create_all(self.__engine)

        # Create the session
        self.__session = sessionmaker(bind=self.__engine)

    def all(self, cls=None):
        """Query all objects based on class"""
        objects = {}
        if cls:
            query = self.__session().query(cls)
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        else:
            for cls in Base.__subclasses__():
                query = self.__session().query(cls)
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects
    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and recreate the database session"""
        Base.metadata.create_all(self.__engine)
        self.scoped___session = (sessionmaker(
            bind=self.__engine,
            expire_on_commit=False))