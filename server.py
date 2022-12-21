"""Server for movie ratings app."""

from flask import Flask, render_template, request, redirect, flash, session
from model import connect_to_db, db
from jinja2 import StrictUndefined
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    return render_template('homepage.html') #has form w/ variable names =uname, pword

@app.route('/movies')
def all_movies():
    movies=crud.get_movies()
    return render_template('all_movies.html', movies=movies) #has form w/ variable names =uname, pword

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details on a particular movie."""
    movie = crud.get_movie_by_id(movie_id)
    return render_template("movie_details.html", movie=movie)

# @app.route('/login')
# def login(email, password):
#     user=crud.create_user()
#     password=request.form.get('password')
#     username=request.form.get('username')
#     return redirect('login', email=email, password=password)

# @app.route('/login')
# def view_movies(email, password):
#     """view list of movies"""
#     user=crud.create_user()
#     password=request.form.get('password')
#     username=request.form.get('username')
#     return redirect('login', email=email, password=password)


if __name__ == "__main__":
    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True, port=5002)
