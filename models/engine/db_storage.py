from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


class DBStorage:
    def __init__(self):
        """Initialize the DBStorage instance."""
        self.__engine = None
        self.__session = None

        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST", default="localhost")
        db = getenv("HBNB_MYSQL_DB")


        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db),
            pool_pre_ping=True
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database"""
        result = {}
        classes = [cls] if cls else [User, State, City, Amenity, Place, Review]

        for class_obj in classes:
            query_result = self.__session.query(class_obj).all()
            for obj in query_result:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result[key] = obj

        return result


    def new(self, obj):
        """Add a new object to the current database session"""
        if obj:
            self.__session.add(obj)
    def save(self):
        """commits changes of the current database session"""
        self.__session.commit()
    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)
    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
