from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv as env
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = env('HBNB_MYSQL_USER')
        passwd = env('HBNB_MYSQL_PWD')
        host = env('HBNB_MYSQL_HOST')
        db = env('HBNB_MYSQL_DB')
        data = 'mysql+mysqldb://{}:{}@{}:3306/{}'\
        .format(user, passwd, host, db)
        self.__engine = create_engine(data, pool_pre_ping=True)

        if env('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def all(self, cls=None):
        from models import storage
        classes = [State, City, User]
        if cls:
            classes = [cls]
        ret = {}
        for _class in classes:
            data = self.__session.query(_class).all()
            for item in data:
                dic = item.to_dict()
                dic.pop('_sa_instance_state', None)
                ret[f"{item.__class__.__name__}.{dic['id']}"] = dic
        return ret

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))



