from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """DBStorage class for SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of DBStorage class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects depending on the class name"""
        from models import classes

        session = self.__session
        objs = {}
        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls)
            for obj in session.query(cls):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objs[key] = obj
        else:
            for name, cls in classes.items():
                if name != "BaseModel":
                    for obj in session.query(cls):
                        key = "{}.{}".format(type(obj).__name__, obj.id)
                        objs[key] = obj
        return objs

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables and current database session"""
        from models import base_model
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
