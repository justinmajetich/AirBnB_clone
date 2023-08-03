import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DatabaseManager:
    __engine = None
    __session = None

    def __init__(self):
        """Method contructor"""
        self.create_engine()

    @classmethod
    def create_engine(cls):
        """Method create engine"""
        if cls.__engine is None:
            mysql_user = os.environ.get("HBNB_MYSQL_USER")
            mysql_password = os.environ.get("HBNB_MYSQL_PWD")
            mysql_host = os.environ.get("HBNB_MYSQL_HOST", "localhost")
            mysql_db = os.environ.get("HBNB_MYSQL_DB")
            pool_pre_ping = True if os.environ.get("HBNB_ENV") == "test" else False

            if all([mysql_user, mysql_password, mysql_db]):
                cls.__engine = create_engine(
                    f"mysql+mysqldb://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}",
                    pool_pre_ping=pool_pre_ping
                )
                Base.metadata.create_all(cls.__engine)
            else:
                raise ValueError("Missing required environment variables for MySQL connection.")

    @property
    def session(self):
        "method that make the connection"
        if self.__session is None:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()
        return self.__session

    def all(self, cls=None):
        """method that print all"""
        objects = {}
        query_classes = [
            User, State, City, Amenity, Place, Review
        ]  # Add the classes corresponding to User, State, City, Amenity, Place, Review

        if cls is None:
            query_classes = query_classes
        else:
            query_classes = [cls]

        for cls in query_classes:
            result = self.__session.query(cls).all()
            for obj in result:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj

        return objects

    def new(self, obj):
        """create a new method"""
        self.__session.add(obj)

    def save(self):
        """Method save"""
        self.__session.commit()

    def delete(self, obj=None):
        """Method delete"""
        if obj:
            self.__session.delete(obj)
