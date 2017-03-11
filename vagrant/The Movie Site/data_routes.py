from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Movie
from cache import cache_movies
from fetching import grab_trailer_url, grab_poster
from utils import get_genre
import json

engine = create_engine('sqlite:///movies.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

data = Blueprint('data', __name__, template_folder='templates')

@data.route('/addNewMovie/', methods=['POST'])
def add_new_movie():
  name = request.form['name'].title()
  year = request.form['year']
  description = request.form['description']
  genreCode = get_genre(request.form.getlist('genre'))
  newMovie = Movie(name=name,
                    year=year,
                    poster=grab_poster(name, str(year)),
                    description=description,
                    trailer=grab_trailer_url(name, str(year)),
                    genre=genreCode,)
  session.add(newMovie)
  session.commit()
  cache_movies(True)
  return json.dumps(newMovie.movie_json)

@data.route('/previewNewMovie/', methods=['POST'])
def preview_new_movie():
  name = request.form['name'].title()
  year = request.form['year']
  description = request.form['description']
  genreCode = get_genre(request.form.getlist('genre'))
  poster=grab_poster(name, str(year))
  trailer=grab_trailer_url(name, str(year))
  newMovie = Movie(name=name,
                    year=year,
                    poster=grab_poster(name, str(year)),
                    description=description,
                    trailer=grab_trailer_url(name, str(year)),
                    genre=genreCode,)
  return json.dumps(newMovie.movie_json)
