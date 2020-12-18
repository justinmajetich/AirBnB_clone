#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


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
