from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """This method initializes the DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(user, pwd, host, db),
            pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """This method returns a dictionary of models currently in storage"""
        from models import classes
        objects = {}
        if cls is None:
            for cls in classes:
                objects.update({obj.id: obj for obj in self.__session.query(cls)})
        else:
            objects = {obj.id: obj for obj in self.__session.query(cls)}
        return objects

    def new(self, obj):
        """This method adds new object to storage"""
        self.__session.add(obj)

    def save(self):
        """This method saves storage to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """This method deletes an object from storage"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """This method reloads storage from database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
