#!/usr/bin/python3
"""Describes a database instance"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """Creates an database instance"""
    __engine = None
    __Session = None

    def __init__(self):
        """Instanciates attributes of the class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get('HBNB_MYSQL_USER'),
            os.environ.get('HBNB_MYSQL_PWD'),
            os.environ.get('HBNB_MYSQL_HOST'),
            os.environ.get('HBNB_MYSQL_DB'),
        ), pool_pre_ping=True)

        metadata = MetaData()

        if os.environ.get('HBNB_ENV') == 'test':
            # get existing tables from the db
            metadata.reflect(bind=self.__engine)

            # Iterate through all the tables
            for table in reversed(metadata.sorted_tables):
                table.drop(self.__engine)

    def all(self, cls=None):
        """Query the db for objs depending on cls name"""
        result = {}

        try:
            if cls is not None:
                objs = self.__Session.query(cls).all()
                for obj in objs:
                    result[f'{cls}.{obj.id}'] = obj
            else:
                all_objs = self.__Session.query().all()
                for obj in all_objs:
                    result[f'{obj.__class__.__name__}.{obj.id}'] = obj
        except Exception as e:
            print(f"Error querying the database: {e}")

        return result

    def new(self, obj):
        """Adds an object to the current session"""
        Session = self.__Session

        with Session() as session:
            session.add(obj)

    def save(self):
        """commit all changes to the db session"""
        Session = self.__Session
        with Session() as session:
            session.commit()

    def delete(self, obj=None):
        """Delete obj if from surrent db session"""
        Session = self.__Session
        if obj is not None:
            with Session() as session:
                session.delete(obj)

    def reload(self):
        """Create tables if they don't exist 
          Also create session
        """
        from models.city import City
        from models.state import State
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        Session_set = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__Session = scoped_session(Session_set)
