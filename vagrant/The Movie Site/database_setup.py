import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    year = Column (Integer(4), nullable=False)
    poster = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    genre = Column(Integer(7), nullable=False)

    @property
    def movie_json(self):
        return {
          'id': self.id,
          'name': self.name,
          'year': self.year,
          'poster': self.poster,
          'description': self.description,
          'genre_code': self.genre,
        }


engine = create_engine('sqlite:///movies.db')

Base.metadata.create_all(engine)