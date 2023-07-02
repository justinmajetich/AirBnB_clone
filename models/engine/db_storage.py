"""New engine DBStorage: (models/engine/db_storage.py)"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base


class DBStorage:
    """private class attributes"""
    __engine = None
    __session = None
    
    """the all important __init__ *bows head*"""
    def __init__(self):
        """link to the user, data retrieved from environment variables"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        """just in case we need it"""
        env = os.getenv('HBNB_ENV')
        
        """
        I MAKe-A the ENGINE! *pASTA hANDS emoJI* 
        uses data grabbed from above 5 lines
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                       .format(user, password, host, database),
                                       pool_pre_ping=True)
        
        """drop all dem der tables if HBNB_ENV is 'test'"""
        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)
        
        """create all dem der tables pardner"""
        Base.metadata.create_all(bind=self.__engine)
        
        """I MaKe_ a the Sesisosion!! XD!1!!!"""
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
        
    def all(self, cls=None):
        from models import classes
        
        objects = {}
        if cls:
            query = self.__session.query(classes[cls])
            for obj in query.all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[key] = obj
                """
                this is the spot where i ate a 
                weed gummy so lets say some prayers
                """
        else:
            for cls in classes.values():
                query = self.__session.query(cls)
                for obj in query.all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects

    """The easy stuff"""
    def new(self, obj):
        self.__session.add(obj)
    
    def save(self):
        self.__session.commit()
    
    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
