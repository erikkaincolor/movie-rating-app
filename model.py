"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """user class"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    email=db.Column(db.String(30), nullable=False, unique = True)
    password=db.Column(db.String(30), nullable=False)

    ratings = db.relationship("Rating", back_populates="user") #user refers to the magic variable in ratings class
    def __repr__(self):
        return f'<User user_id= {self.user_id} email={self.email} password={self.password}>'




class Movie(db.Model):
    """user movie"""
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement= True, primary_key=True)
    title=db.Column(db.Text, nullable = False)
    overview=db.Column(db.Text, nullable = False)
    release_date=db.Column(db.DateTime, nullable = False)
    poster_path=db.Column(db.String, nullable = False)

    ratings = db.relationship("Rating", back_populates="movie") #movie refers to the magic variable in ratings class

    def __repr__(self):
        return f'<Movie movie_id= {self.movie_id} title={self.title}>'

class Rating(db.Model):
    """rating class for middle table rating"""
    __tablename__="ratings"

    rating_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    score=db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id")) #################### these need to be added too!
    movie_id  = db.Column(db.Integer, db.ForeignKey("movies.movie_id")) ################## these need to be added too!

    movie = db.relationship("Movie", back_populates="ratings")  #ratings referes to the magic variable in the movie class 
    user = db.relationship("User", back_populates="ratings")  #ratings referes to the magic variable in the user class 
    
    
    # movie = db.Relationship(Movie, backref="rating")
    # rating_id = db.Relationship(Movie, backref="rating")
    
    def __repr__(self):
        return f'<Rating rating_id= {self.rating_id} score={self.score}>'

    

def connect_to_db(app, db_uri="postgresql:///ratings", echo=True):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = echo
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    
    with app.app_context():
        connect_to_db(app)
    # import os
    # os.system(f'dropdb ratings --if-exists')
    # os.system(f'createdb ratings')
    # db.create_all() 
    # test_user = User(email='erikka@test.com', password='1234')
    # #mov=Movie(title='Test Movie', overview="About a movie.", release_date=datetime.now(), poster_path="blah")    # rating1=Rating(score=3, user=test_user, movie=test_movie) 
    # #rat1=Rating(score=5, user=test_user, movie=movies[0])
    # db.session.add(test_user) #to create and add
    # # db.session.add(test_movie) #to create and add
    # # db.session.add(rating1) #to create and add
    # # instances=[test_user, test_movie, rating1]
    # # db.session.add_all(instances)
    # db.session.commit()
