"This file manipulates the data in the db, saves to it, and reads/queries it via execution functions"

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

    user = User(email, password)

    return user





















#crud.py deals with db connections, this dunder main will connect you to the database when you run crud.py interactively
if __name__ == '__main__':
    from server import app
    with app.app_context():
        connect_to_db(app)
    import os
    # create_user('erokk@', '124')
    # db.session.add()
    # db.session.commit()
    create_user('erikka', '121e')
    
