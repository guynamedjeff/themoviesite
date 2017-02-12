from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Movie

import memcache
import logging

engine = create_engine('sqlite:///movies.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

mc = memcache.Client(['127.0.0.1'], debug=0)

def cache_movies(update = False):
    key = 'archive'
    movies = mc.get(key)
    if movies is None or update:
        logging.error("DB QUERY")
        movies = session.query(Movie).all()
        mc.set(key, movies)
    return movies

# CACHE1 = {}
# def cache_movies(update = False):
#     key = 'archive'
#     if not update and key in CACHE1:
#         movies = CACHE1[key]
#     else:
#         logging.error("DB QUERY")
#         movies = session.query(Movie).all()
#         CACHE1[key] = movies
#     return movies