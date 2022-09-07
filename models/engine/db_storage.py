#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage:
	"""New bdstorage engine"""
	__engine = None
	__session = None
	classes = {
		'BaseModel': BaseModel, 'User': User, 'Place': Place,
		'State': State, 'City': City, 'Amenity': Amenity,
		'Review': Review
	}

	def __init__(self):
		"""Engine constructor"""
		self.__engine = create_engine(
			'mysql+mysqldb://{}:{}@{}/{}'.format(
				getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
				getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
			pool_pre_ping=True)
		metadata = MetaData()
		if getenv('HBNB_ENV') == 'test':
			metadata.drop_all(bind=self.__engine)

	def all(self, cls=None):
		"""All method"""
		dict_cls = {}
		if cls:
			query = self.__session.query(cls).all()
			for key, value in query.items():
				dict_cls[key] = value
		else:
			for CLS in self.classes:
				query = self.__session.query(CLS).all()
				for key, value in query.items():
					dict_cls[key] = value
		return (dict_cls)

	def new(self, obj):
		"""New method"""
		self.__session.add(obj)

	def save(self):
		"""Save method"""
		self.__session.commit()

	def delete(self, obj=None):
		"""Delete method"""
		if obj:
			self.__session.delete(obj)

	def reload(self):
		"""Reload method"""
		Base.metadata.create_all(self.__engine)
		session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
		Session = scoped_session(session_factory)
		self.__session = Session()

