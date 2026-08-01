#!/usr/bin/python3
"""State model module, with its relationship to the cities.

This module defines the ``State`` class, mapped to the ``states`` table
of the database, and the ``Base`` instance every model inherits from.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represent a state of the ``states`` table.

    Attributes:
        id: The unique identity of the state, its primary key.
        name: The name of the state, at most 128 characters.
        cities: The cities of the state, deleted along with it.
    """

    __tablename__ = "states"
    id = Column(Integer, nullable=False, unique=True, primary_key=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
