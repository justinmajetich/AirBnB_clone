#!/usr/bin/python3
"""
Scripts to drop database incase of changes in models
"""


import os
from sqlalchemy import create_engine
from models.base_model import Base

def get_engine_url():
        """
        Generate the db engine url based on env variables
        """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        return f'mysql+mysqldb://{user}:{password}@{host}/{database}'

# Replace 'your_database_uri' with the URI of your actual database
print(get_engine_url())
engine = create_engine(get_engine_url())

# Drop Tables
Base.metadata.drop_all(engine)

print("Tables dropped successfully.")

