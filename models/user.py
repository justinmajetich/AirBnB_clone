#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models
import sqlalchemy


class User(BaseModel, Base):
    """This class defines a user by various attributes
        Attributs:
        ====================
            email : email of user
                    String, not null
            password: password of compte user
                    String, not null
            first_name : name of user
                    String, not null
            last_name: last name of user
                    String, not null
    """
    __tablename__ = "users"
    # if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    email = Column(
        String(128),
        nullable=False)
    password = Column(
        String(128),
        nullable=False
    )
    first_name = Column(
        String(128),
        nullable=False,
        default=""
    )
    last_name = Column(
        String(128),
        nullable=False,
        default=""
    )
    places = relationship(
        "Place",
        backref="user",
        cascade="all, delete-orphan")
    reviews = relationship(
        "Review",
        backref="user",
        cascade='all, delete-orphan')
    # else:
    #     email = ""
    #     password = ""
    #     first_name = ""
    #     last_name =""