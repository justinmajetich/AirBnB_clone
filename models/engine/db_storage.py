#!/usr/bin/python3
<<<<<<< HEAD
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()

=======
"""database storage engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base
from os import getenv

if getenv("HBNB_TYPE_STORAGE"):
	from models.place import place_amenity

classes = {"User": User, "State": State, "City": City, "Amenity": Amenity,
	   "Place": Place, "Review": Review}


class DBStorage:
	"""database storage engine for mysql"""
	__engine = None
	__session = None

	def __init__(self):
		"""initiate new dbstorage instance"""
		HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
		HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
		HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
		HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
		HBNB_ENV = getenv('HBNB_ENV')
		self.__engine = create_engine(
			'mysql+mysqldb://{}:{}@{}/{}'.format(
						HBNB_MYSQL_USER,
						HBNB_MYSQL_PWD,
						HBNB_MYSQL_HOST,
						HBNB_MYSQL_DB
					), pool_pre_ping=True)
		if HBNB_ENV == 'test':
			Base.metadata.drop_all(self.__engine)

	def all(self, cls=None):
		"""query on the current db session of all the cls objects"""
		dct = {}
		if cls is None:
			for c in classes.values():
				objs = self.__session.query(c).all()
				for obj in objs:
					key = obj.__class__.__name__ + '.' + obj.id
					dct[key] = obj
		else:
			objs = self.__session.query(cls).all()
			for obj in objs:
				key = obj.__class__.__name__ + '.' + obj.id
				dct[key] = obj
			return dct

	def new(self, obj):
		"""adds the obj to the current db session"""
		if obj is not None:
			try:
				self.__session.add(obj)
				self.__session.flush()
				self.__session.refresh(obj)
			except Exception as ex:
				self.__session.rollback()
				raise ex

	def save(self):
		"""commit all the changes to the current db session"""
		self.__session.commit()

	def delete(self, obj=None):
		"""deletes from the current db session the obj """
		if obj is not None:
			self.__session.query(type(obj)).filter(type(
				     obj).id == obj.id).delete()

	def reload(self):
		"""reloads the database"""
		Base.metadata.create_all(self.__engine)
		session_factory = sessionmaker(bind=self.__engine,
					       expire_on_commit=False)

	def close(self):
		"""closes the working sqlalchemy session"""
		self.__session.close()
>>>>>>> 3b9a1fe3245063d3054475ac3c4b9f0160fd3ce4
