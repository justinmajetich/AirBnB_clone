#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


<<<<<<< HEAD
class User(BaseModel):
    """This class defines a user
		Attributes:
			email -> email address
			password -> don't look silly
			first_name -> John
			last_name -> Smith
	"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
=======
class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship('Place',
                          cascade='all,delete',
                          backref='user')
    reviews = relationship('Review',
                           cascade='all,delete',
                           backref='user')
>>>>>>> 7a38b0fde34d61e1bb21423f8dfa398ec535d750
