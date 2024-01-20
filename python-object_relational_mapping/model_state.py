# model_state.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class representing a state in the database.

    Attributes:
        id (int): Auto-generated unique integer, primary key.
        name (str): String with a maximum of 128 characters, cannot be null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, doc="Auto-generated unique integer, primary key.")
    name = Column(String(128), nullable=False, doc="String with a maximum of 128 characters, cannot be null.")
