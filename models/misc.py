from os import getenv

# Contains most variables
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review

classes = {
    'User': User,
    'City': City,
    'Place': Place,
    'Review': Review,
    'State': State,
}

DB_NAME = getenv("HBNB_MYSQL_DB")
HOST = getenv("HBNB_MYSQL_HOST")
USERNAME = getenv("HBNB_MYSQL_USER")
PASSWORD = getenv("HBNB_MYSQL_PWD")
ENV = getenv("HBNB_ENV")
