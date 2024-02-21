
#!/usr/bin/python3
"""Defines a DB storage engine"""
import os
from sqlalchemy import create_engine


sql_user = os.environ.get("HBNB_MYSQL_USER")
sql_pass = os.environ.get("HBNB_MYSQL_PWD")
sql_host = os.environ.get("HBNB_MYSQL_HOST")
sql_db = os.environ.get("HBNB_MYSQL_DB")

class DBStorage:
    """An engine to manage database storage mechanisms"""
    __engine = None
    __session = None

    def __init__(self):
        conn_params = f"mysql+mysqldb://{sql_user}:{sql_pass}@{sql_host}/{sql_db}"
        self.__engine = create_engine(conn_params, pool_pre_ping=True)

        test_env = os.environ.get("HBNB_ENV")
        if test_env == "test":
            self.__engine.meta.drop_all()
    
    def all(self, cls=None):
        """Queries the database and reeturns all models"""
        if cls is None:
            objects = {}
        objects = self.__session().all(cls)
