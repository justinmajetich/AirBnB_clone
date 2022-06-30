#!/usr/bin/python3
"""test database
"""
import unittest
from sqlalchemy import create_engine
import os
from models.base_model import Base

class test_db_storage(unittest.TestCase):
    """ this class sets up the enviornment for dbTesting
    """
    @classmethod
    def setUpClass(self, cls):

        dialect = "mysql"
        driver = "mysqldb"
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'
                                .format(dialect, driver, user, passwd, host,
                            db), pool_pre_ping=True)

    def test_db(self):
        """written test "Oh My!"
        """
        self.assertEqual (db, "HBNB_MYSQL_DB")
