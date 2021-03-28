#!/usr/bin/python3
"""
Defines a class City that link to the MySQL table 'cities' using SQLAlchemy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """
    Class that links to MySQL table 'cities'.
    Class instance :
        id : Integer  primary_key
        name: String(128)
        state_id: Integer, Foreign_Key(states.id)
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
