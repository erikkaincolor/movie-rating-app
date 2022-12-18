"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    title=movie["title"]
    overview=movie["overview"]
    poster_path=movie["poster_path"]

    format="%Y-%m-%d"

    release_date=datetime.strptime(movie["release_date"], format)

    db_movie=crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

model.db.session.add_all(movies_in_db)
model.db.session.commit()





x=10 #how do i stop it from making 100 rows
# for _ in range(10)
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'
    
    db_user=crud.create_user(email, password)
    model.db.session.add(db_user)

# Use choice to get a random movie from movies_in_db and 
# use randint to generate a random number between 1–5. 

    
    for x in range(10): ####i missed this
        random_movie=choice(movies_in_db)
        score=randint(1, 5)
        db_rating=crud.create_rating(db_user, random_movie, score)
        model.db.session.add(db_rating)

model.db.session.commit() #i keep including in the for loop 