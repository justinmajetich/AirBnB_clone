#!/usr/bin/python3
"""new engine"""

from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage:
    """
    storage engine for db
    """
    __engine = None
    __session = None

    all_classes = [City, State, Place, Review, Amenity, User]

    def __init__(self):
        """
        called when new instance is created
        """
        user = environ.get("HBNB_MYSQL_USER")
        pwd = environ.get("HBNB_MYSQL_PWD")
        host = environ.get("HBNB_MYSQL_HOST", "localhost")
        db = environ.get("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:3306/{}"
            .format(user, pwd, host, db),
            pool_pre_ping=True
        )

        if environ.get("HBNB_ENV") == "test":
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on current db session
        """
        if cls:
            results = {}
            for record in self.__session.query(cls).all():
                key = f"{record.to_dict()['__class__']}.{record.id}"
                results.update({key: record})
            return results

        results = {}
        for _class in self.all_classes:
            try:
                for record in self.__session.query(_class).all():
                    key = f"{record.to_dict()['__class__']}.{record.id}"
                    results.update({key: record})
            except sqlalchemy.exc.SQLAlchemyError:
                continue
        return results

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        create the current database session from the engine"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)