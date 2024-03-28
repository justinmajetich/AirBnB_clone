from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.user import User
from models.place import Place
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Create an engine and link to MySQL database
        """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects by class name."""
        new_objects = {}
        if cls:
            new_objects = {obj.__class__.__name__ + '.' + obj.id:
                           obj for obj in self.__session.query(cls)}
        else:
            for clsn in Base.__subclasses__():
                new_objects.update({obj.__class__.__name__ + '.' + obj.id:
                                    obj for obj in self.__session.query(clsn)})
        return new_objects

    def new(self, obj):
        """Adds the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and the session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
