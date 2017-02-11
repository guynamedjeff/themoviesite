from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Movie
app = Flask(__name__)

engine = create_engine('sqlite:///movies.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/movies/json/')
def json():
    movies = session.query(Movie).all()
    return jsonify(Movies=[m.movie_json for m in movies])

@app.route('/')
@app.route('/movies/')
def main():
    movies = session.query(Movie).all()
    return render_template("index.html", movies=movies)

@app.route('/movies/<int:movie_id>/')
def movieDetails(movie_id):
    movie = session.query(Movie).filter_by(id=movie_id).one()
    return render_template("movie.html", movie=movie)

@app.route('/movies/new/', methods=['GET', 'POST'])
def newMovie():
    if request.method =='POST':
      newMovie = Movie(name=request.form['name'],
                        year=request.form['year'],
                        poster=request.form['poster'],
                        genre=request.form['genre'])
      session.add(newMovie)
      session.commit()
      flash(newMovie.name + " has been added.")
      return redirect(url_for('main'))
    else:
      return render_template("newmovie.html")

@app.route('/movies/<int:movie_id>/edit/', methods=['GET', 'POST'])
def editMovie(movie_id):
    movie = session.query(Movie).filter_by(id=movie_id).one()
    if request.method =='POST':
      if request.form['name']:
        movie.name = request.form['name']
      if request.form['year']:
        movie.year = request.form['year']
      if request.form['poster']:
        movie.poster = request.form['poster']
      if request.form['genre']:
        movie.genre = request.form['genre']
      session.add(movie)
      session.commit()
      flash(movie.name + " has been edited.")
      return redirect(url_for('main'))
    else:
      return render_template("editmovie.html", movie=movie)

@app.route('/movies/<int:movie_id>/delete/', methods=['GET', 'POST'])
def deleteMovie(movie_id):
    movie = session.query(Movie).filter_by(id=movie_id).one()
    if request.method =='POST':
      session.delete(movie)
      session.commit()
      flash(movie.name + " has been deleted.")
      return redirect(url_for('main'))
    else:
      return render_template("deletemovie.html", movie=movie)

if __name__ == '__main__':
    app.secret_key = 'american_beauty'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)