from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Movie

import redis
import logging
import json

engine = create_engine('sqlite:///movies.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Upon data update or no data, replaces the cache with latest DB info.
# Returns a list from stored redis data.
def cache_movies(update = False):
    key = 'archive'
    data = get_data_dump(key)
    if not data or update:
        logging.error("DB QUERY")
        delete_data()
        set_data(key)
        data = get_data_dump(key)
    return data

# Returns a list of decoded JSON strings stored in redis.
def get_data_dump(key):
    data = []
    movies = r.lrange(key,0,-1)
    for m in movies:
        data.append(json.loads(m))
    return data

# Encodes and stores JSON strings in redis.
def set_data(key):
    movies = session.query(Movie).all()
    for m in movies:
        mStr = json.dumps(m.movie_json)
        r.lpush(key, mStr)
    return

# Delete all data in redis.
def delete_data():
    r.flushall()
    return

# Legacy code from an earlier iteration featuring memcache for main page 'simple users'.

# import memcache

# mc = memcache.Client(['127.0.0.1'], debug=0)

# def cache_movies(update = False):
#     key = 'archive'
#     movies = mc.get(key)
#     if movies is None or update:
#         logging.error("DB QUERY")
#         movies = session.query(Movie).all()
#         mc.set(key, movies)
#     return movies