"This file manipulates the data in the db, saves to it, and reads/queries it via execution functions"

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


def create_user(email, password):
    """Create and return a new user."""
    user = User(email=email, password=password)
    # db.session.add(user)
    # db.session.commit()
    return user

# >>> user1=create_user(email="era@emwef", password="password1")
# >>> db.session.add(user1)
# >>> db.session.commit()

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""
    from datetime import datetime
    movie=Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)    
    # db.session.add(movie)
    # db.session.commit()
    return movie

# >>> from datetime import datetime                  
# >>> mo=create_movie(title='Test Movie', overview="About a movie.", release_date=datetime.now(), poster_path="blah")
# >>> db.session.add(mo)
# >>> db.session.commit()     
 

def create_rating(user, movie, score):
    """create a rating of a movie"""
    rating=Rating(user=user, movie=movie, score=score)
    return rating

# >>> test=create_rating(user=user1, movie=mo, score=7)
# >>> db.session.add(test)
# >>> db.session.commit()   












#crud.py deals with db connections, this dunder main will connect you to the database when you run crud.py interactively
if __name__ == '__main__':
    from server import app
    with app.app_context():
        connect_to_db(app)
    
    # create_user('erokk@', '124')
    # db.session.add()
    # db.session.commit()
    
    
