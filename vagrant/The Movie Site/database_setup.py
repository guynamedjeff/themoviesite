import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    year = Column (Integer(4), nullable=False)
    poster = Column(String(250), nullable=False)
    genre = Column(Integer(7), nullable=False)

engine = create_engine('sqlite:///movies.db')

Base.metadata.create_all(engine)