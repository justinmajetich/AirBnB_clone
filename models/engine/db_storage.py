#!/usr/bin/python3
"""
Module defines DBStorage class for HBNB project
"""


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from os import getenv


class DBStorage:
    """
    DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Create a new instance of DBStorage
        """
        storage_type = getenv("HBNB_TYPE_STORAGE", "file")

        if storage_type == "db":
            self.__setup_db_storage()
        else:
            self.__setup_file_storage()

    def __setup_db_storage(self):
        """Set up database storage"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        self.__initialize_session()

    def __setup_file_storage(self):
        """Set up file-based storage"""
        # Additional setup for file-based storage can be added here
        pass

    def __initialize_session(self):
        """Initialize database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def all(self, cls=None):
        """Query all objects of a certain class"""
        objs = {}
        if cls:
            for obj in self.__session.query(cls):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objs[key] = obj
        else:
            for table in Base.metadata.tables.keys():
                for obj in self.__session.query(eval(table)):
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objs[key] = obj
        return objs

    def new(self, obj):
        """Add a new object to the database"""
        self.__session.add(obj)

    def save(self):
        """Save all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload all objects from the database"""
        self.__initialize_session()

    def close(self):
        """Close the current session"""
        self.__session.close()


if __name__ == "__main__":
    DBStorage()
