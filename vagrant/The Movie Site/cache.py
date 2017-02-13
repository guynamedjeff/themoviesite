from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Movie

import redis
# import memcache
import logging
import json

engine = create_engine('sqlite:///movies.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def cache_movies(update = False):
    key = 'archive'
    items = []
    movies = r.lrange(key,0,-1)
    for m in movies:
        items.append(json.loads(m))
    if not movies or update:
        logging.error("DB QUERY")
        r.flushall()
        movies = session.query(Movie).all()
        for m in movies:
            mStr = json.dumps(m.movie_json)
            r.lpush(key, mStr)
        movies = r.lrange(key,0,-1)
        for m in movies:
            items.append(json.loads(m))
    return items

def get_data_dump(movies):
    data = []
    movies = r.lrange(key,0,-1)
    for m in movies:
        data.append(json.loads(m))
    return data

# mc = memcache.Client(['127.0.0.1'], debug=0)

# def cache_movies(update = False):
#     key = 'archive'
#     movies = mc.get(key)
#     if movies is None or update:
#         logging.error("DB QUERY")
#         movies = session.query(Movie).all()
#         mc.set(key, movies)
#     return movies