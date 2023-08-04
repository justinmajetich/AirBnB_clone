from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Relationship with the Place class
    places = relationship(
        'Place',
        backref=backref('user', cascade='all, delete-orphan'),
        cascade='all, delete-orphan'
    )

    # Relationship with the Review class
    reviews = relationship(
        'Review',
        backref=backref('user', cascade='all, delete-orphan'),
        cascade='all, delete-orphan'
    )
