#!/usr/bin/python3

"""
This module defines a class to
manage db storage for hbnb clone
"""


from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import environ

# Comment after use
from icecream import ic

# Loading environment variables from .env to os
load_dotenv("../../.env")

# Reading and saving in variables from os environ
env_type = environ.get("HBNB_ENV")
username = environ.get("HBNB_MYSQL_USER")
password = environ.get("HBNB_MYSQL_PWD")
hostaddr = environ.get("HBNB_MYSQL_HOST")
database = environ.get("HBNB_MYSQL_DB")
storage_ = environ.get("HBNB_TYPE_STORAGE")
dialect_ = environ.get("HBNB_DIALECT")
dbdriver = environ.get("HBNB_DRIVER")


# engine variables
str_symb = ["+", "://", ":", "@", "/"]
str_vars = dialect_ + str_symb[0] + dbdriver
str_vars += str_symb[1] + username + str_symb[2]
str_vars += password + str_symb[3] + hostaddr
str_vars += str_symb[4] + database

# ic debugging variable checker
# comment after use
ic(
    env_type,
    username,
    password,
    hostaddr,
    database,
    storage_,
    dialect_,
    dbdriver,
    str_vars)

# sqlalchemy engine
engine = create_engine(str_vars)

# class DBStorage():
#     __engine = None
#     __session = None

#     def __init__(self):
