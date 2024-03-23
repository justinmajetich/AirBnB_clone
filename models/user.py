#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
import sys


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128), nullable=False)
    last_name = Column('last_name', String(128), nullable=False)

    def create_user(email, password, first_name, last_name):
        """Function to create a user"""
        engine = create_engine('sqlite:///user_database.db', echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
    
        new_user = User(email=email, password=password, first_name=first_name, last_name=last_name)
        session.add(new_user)
        session.commit()
        session.close()

    if __name__ == "__main__":
        if len(sys.argv) != 5:
            print("Usage: python script_name.py email password first_name last_name")
        else:
            email = sys.argv[1]
            password = sys.argv[2]
            first_name = sys.argv[3]
            last_name = sys.argv[4]
            create_user(email, password, first_name, last_name)