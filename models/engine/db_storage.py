from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError
from models.base_model import Base

class DBStorage:
    """Database storage engine using SQLAlchemy"""
    __engine = None
    __session = None

def __init__(self):
    """Creates a new instance of DBStorage"""
    user = os.environ.get('HBNB_MYSQL_USER')
    password = os.environ.get('HBNB_MYSQL_PWD')
    host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
    database = os.environ.get('HBNB_MYSQL_DB')
    self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}', pool_pre_ping=True)
  
    if os.environ.get('HBNB_ENV') == 'test':
        Base.metadata.drop_all(self.__engine)

def all(self, cls=None):
    """query on the current database session all objects depending of the class name"""
    from models import classes
    objects = {}
    if cls:
            query = self.__session.query(classes[cls]).all()
            for obj in query:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        else:
            for class_name in classes.keys():
                query = self.__session.query(classes[class_name]).all()
                for obj in query:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        return objects

def new(self, obj):
    """Add the object to the current database session"""
    self.__session.add(obj)

def save(self):
    """Commit all changes of the current database session"""
    self.__session.commit()

def delete(self, obj=None):
    """Delete from the current database session"""
    if obj
        self.__session.delete(obj)

def reload(self):
    """Create all tables in the database and create the current database session"""
    Base.metadata.create_all(self.__engine)
    Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

def close(self):
        """Close the session"""
        self.__session.remove()

    
     

