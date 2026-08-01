#!/usr/bin/python3
"""City model module, used with the relationship of the State class.

This module defines the ``City`` class, mapped to the ``cities`` table
of the database, which points to the state the city belongs to.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base


class City(Base):
    """Represent a city of the ``cities`` table.

    Attributes:
        id: The unique identity of the city, its primary key.
        name: The name of the city, at most 128 characters.
        state_id: The identity of the state the city belongs to.
    """

    __tablename__ = "cities"
    id = Column(Integer, nullable=False, unique=True, primary_key=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
