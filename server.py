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

#######################################################
#######################################################
#######################################################

@app.route('/movies')
def all_movies():
    movies=crud.get_movies()
    return render_template('all_movies.html', movies=movies) #has form w/ variable names =uname, pword

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details on a particular movie."""
    movie = crud.get_movie_by_id(movie_id)
    session["movie_id"]=movie.movie_id #?????????????????????????????
    return render_template("movie_details.html", movie=movie)

#######################################################
#######################################################
#######################################################

@app.route("/users")
def show_users(): #DONE, for server
    """show users"""
    users=crud.get_users()
    return render_template("users.html", users=users)

@app.route("/users", methods=['POST'])
def account_creation(): #DONE, for server
    """create user"""
    email=request.form.get('email')
    password=request.form.get('password')

    user=crud.get_user_by_email(email)
    if user:
        flash("you can’t create an account with that email, try again")
    else:
        flash("Your account was created successfully and you can now log in.")
        new_user=crud.create_user(email, password)
        db.session.add(new_user)
        db.session.commit()
    return redirect("/")

@app.route("/users/<user_id>")
def show_profile(user_id): #DONE, for server
    """deets on particular user"""
    user=crud.get_user_by_id(user_id)####
    return render_template("user-profile.html", user=user)


@app.route('/', methods=["POST"])
def login():
    """user login"""
    email=request.form.get("email")
    password=request.form.get("password")
    user=crud.get_user_by_email(email)
    if user.password==password: 
        if user:
            flash(f"Logged in!")
            session["current_email"]=user.email #logged in if session is in route
            flash(f"Welcome back, {user.email}!")
    else: #    if not user or user.password != password:
        flash("Please try again.")
    return redirect("/")


#######################################################
#######################################################
#######################################################


#####needed the most help here, spent about 3 hours total 
#figure out where input is coming from in html! either user profile or movie deets
@app.route("/update_rating", methods=["POST"])
def update_rating():
    """where ratings are updated"""
    rating_id = request.json["rating_id"] #?
    #AJAX
    #incorrect:rating=crud.update_rating(new_rating, rating.id)

    updated_score = request.json["updated_score"]
    #AJAX: i was wondering where to get it from, this is ajax versus form 

    crud.update_rating(rating_id, updated_score)
    #incorrect/didnt need to be in a variable:         rating=crud.update_rating(new_rating, rating.id)
    
    db.session.commit()
    return "Success"



@app.route("/movies/<movie_id>/ratings", methods=["POST"])
def create_ratings(movie_id): #DONE, for server
    """create movie rating on movie page"""
    #INCORRECT: return render_template("user-profile.html", rating=rating)
    
    logged_in_email = session.get("current_email")
    #INCORRECT:  user=session["current_user"] they logged in via email

    rating_score = request.form.get("rating")
    #this form is in the movie deets html

    if logged_in_email is None:
        flash("You must log in to rate a movie.")
    elif not rating_score: #if theres no score, see if required or not
        flash("Error: you didn't select a score for your rating.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        #^refer to session to see whos logged in
        
        movie = crud.get_movie_by_id(movie_id)
        #^get movie id from parameters

        rating = crud.create_rating(user, movie, int(rating_score))
        #^create rating

        db.session.add(rating)
        db.session.commit()

        flash(f"You rated this movie {rating_score} out of 5.")

    return redirect(f"/movies/{movie_id}")








if __name__ == "__main__":
    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True, port=5003)
