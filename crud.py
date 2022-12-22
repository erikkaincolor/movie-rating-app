"This file manipulates the data in the db, saves to it, and reads/queries it via execution functions"

#  utility functions for creating data. 


# >>> db.session.rollback()<------incase of error

#creating new data, 
# retrieving data that already exists, 
# updating data, 
# and deleting data.


# (Step 1: the C, U, and D in CRUD functionality) 
# Manipulating an object/instance with sqlalchemy via python3 
# In Part 2, you’ll write utility functions to make 
# creating, retrieving, and updating the database a lot more convenient. 

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password): #DONE
    """Create and return a new user."""
    user = User(email=email, password=password)
    # db.session.add(user)
    # db.session.commit()
    return user

# >>> user1=create_user(email="era@emwef", password="password1")
# >>> db.session.add(user1)
# >>> db.session.commit()

def get_users(): #DONE, for server
    return User.query.all()



def get_user_by_id(user_id): #DONE, for server
    return User.query.get(user_id) #####


def get_user_by_email(email):
    return User.query.filter(User.email==email).first()














def create_movie(title, overview, release_date, poster_path): #DONE
    """Create and return a new movie."""
    from datetime import datetime
    movie=Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)    
    # db.session.add(movie) #will mess up atomicity
    # db.session.commit() #will mess up atomicity
    return movie

# >>> from datetime import datetime                  
# >>> mo=create_movie(title='Test Movie', overview="About a movie.", release_date=datetime.now(), poster_path="blah")
# >>> db.session.add(mo) #will mess up atomicity
# >>> db.session.commit()  #will mess up atomicity

def get_movies(): #DONE, for seed
    """this will get all movie data"""
    return Movie.query.all()
 
def get_movie_by_id(movie_id): #DONE, for server
    return Movie.query.get(movie_id)
    # return Movie.query.get(movie_id)



def create_rating(user, movie, score): #DONE
    """create a rating of a movie..seed db side abd server side"""
    rating=Rating(user=user, movie=movie, score=score)
    return rating


def update_rating(rating_id, new_rating):
    """ Update a rating given rating_id and the updated score. """
    old_rating = Rating.query.get(rating_id) #<----get old rating object by PK
    old_rating.score = new_rating 
    return new_rating

    
#wheres each part of the function coming from?
#server: crud.get_user_by_id(user_id) <---user_id came from clicking on list item in template
#db:user_id was queried in db to fetch user

#server: 
#seed: crud.create_rating(user, movie, score) <---used to create fake ratings in db....

# >>> test=create_rating(user=user1, movie=mo, score=7)
# >>> db.session.add(test) #will mess up atomicity
# >>> db.session.commit()   #will mess up atomicity 












#crud.py deals with db connections, this dunder main will connect you to the database when you run crud.py interactively
if __name__ == '__main__':
    from server import app
    with app.app_context():
        connect_to_db(app)
    
    # create_user('erokk@', '124')
    # db.session.add()
    # db.session.commit()
    
    
