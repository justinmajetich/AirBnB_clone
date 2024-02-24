from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base


class DBStorage:
    """ DBStorage class of clone """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DBStorage """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB'),
                pool_pre_ping=True
            )
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )()

    def all(self, cls=None):
        """Query on the current database session"""
        if cls:
            return {
                str(cls.__name__) + '.' + str(obj.id): obj
                for obj in self.__session.query(cls).all()
            }
        else:
            return {
                str(cls.__name__) + '.' + str(obj.id): obj
                for cls in Base._decl_class_registry.values()
                for obj in self.__session.query(cls).all()
            }

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)
        self.__session.commit()

    def reload(self):
        """Create all tables in the database"""
        self.__session = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )()
