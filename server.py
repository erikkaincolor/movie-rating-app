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

@app.route('/', methods=["POST"])
def login():
    email=request.form.get("email")
    password=request.form.get("password")
    user=crud.get_user_by_email(email)
    if user.password==password:
        if user:
            flash(f"Logged in!")
            session["current_user"]=user.user_id
            return redirect(f'/users/<user_id>') #has form w/ variable names =uname, pword
    else:
        flash("Please try again.")
        return redirect("/")


@app.route('/movies')
def all_movies():
    movies=crud.get_movies()
    return render_template('all_movies.html', movies=movies) #has form w/ variable names =uname, pword

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details on a particular movie."""
    movie = crud.get_movie_by_id(movie_id)
    session["movie_id"]=movie.movie_id
    return render_template("movie_details.html", movie=movie)

@app.route("/users")
def show_users(): #DONE, for server
    users=crud.get_users()
    return render_template("users.html", users=users)

@app.route("/users", methods=['POST'])
def account_creation(): #DONE, for server
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
        
@app.route("/users/<user_id>/<rating_id>", methods=["POST"])
def show_profile(user_id): #DONE, for server
    user=crud.get_user_by_id(user_id)####
    # answer=request.form("favorited")
    # favorite=crud.add_fave(answer)
    # if favorite.:
    #     do this
    movie_id=session["movie_id"]
    score=request.form("rating")
    rating=crud.create_rating(score)

    #on the movie detail page, you click forms 
    # button, route that score to favoirte 
    # route on profile

    #you take score from form and put it in a 
    # crud.rate_movie(score) and that gives u the id
    
    #user from session somehow

    #movie from movie detail page, thats y i want to put session on that page


    return render_template("user-profile.html", user=user)

# update_rating(rating_id, new_rating)





if __name__ == "__main__":
    connect_to_db(app)

    app.run(host="0.0.0.0", debug=True, port=5003)
