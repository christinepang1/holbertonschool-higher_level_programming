#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import State, Base


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
