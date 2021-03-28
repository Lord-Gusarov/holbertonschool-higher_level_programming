#!/usr/bin/python3
"""
Defines a class State that link to the MySQL table 'states' using SQLAlchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """
    Class that links to MySQL table 'states'.
    Class instance :
        id : Integer  primary_key
        name: String(128)
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state',
                          cascade='all, delete, delete-orphan')
