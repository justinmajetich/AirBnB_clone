#!/user/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


class DBStorage:
    __engine = None
    __session = None
    _FileStorage__objects = {}

    def __init__(self):
        """Create the engine and session for database interaction."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query objects from the current session."""
        from models import classes  # Import all classes here

        objects = {}

        if cls is not None:
            if type(cls) is str:
                cls = classes[cls]
            objects_list = self.__session.query(cls)
        else:
            objects_list = []
            for class_name, class_type in classes.items():
                objects_list += self.__session.query(class_type).all()

        for obj in objects_list:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects[key] = obj

        return objects

    def new(self, obj):
        """Add an object to the current session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and session."""
        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()
