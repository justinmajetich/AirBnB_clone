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
from models.engine.file_storage import FileStorage


class DBStorage(FileStorage):
    """ Defines the class DBStorage """
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
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            objects_list = self.__session.query(cls)
        else:
            objects_list = self.__session.query(State).all()
            objects_list.extend(self.__session.query(City).all())
            objects_list.extend(self.__session.query(User).all())
            objects_list.extend(self.__session.query(Place).all())
            objects_list.extend(self.__session.query(Review).all())
            objects_list.extend(self.__session.query(Amenity).all())
        obj_dict = {}    
        for obj in objects_list:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict

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
