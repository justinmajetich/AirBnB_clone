from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
import os 

class DBStorage:
  """[DBStorage]"""
  __engine = None
  __session = None

  __init__(self):
    """__init__"""
    user = os.getenv('HBNB_MYSQL_USER')
    password = os.getenv('HBNB_MYSQL_PWD')
    host = os.getenv('HBNB_MYSQL_HOST')
    database = os.getenv('HBNB_MYSQL_DB')
    environment = os.getenv('HBNB_ENV')


    self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), pool_pre_ping=True)

    if environment == 'test':
      Base.metadata.drop_all(self.__engine)

  def all(self, cls=None):
    sesion = sessionmaker(self.__engine)
    ses = sesion()