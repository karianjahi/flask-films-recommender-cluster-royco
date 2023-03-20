
import random

movies = [
    "The Shawshank Redemption",
    "Star Wars: Episode IV - A New Hope",
    "Pulp Fiction",
    "The Dark Knight",
    "Forrest Gump",
    "Inception",
    "The Matrix",
    "Saving Private Ryan",
    "Casablanca",
    "The Lion King"
    ]

def get_recommendation():
    random.shuffle(movies)
    return movies[:3]

def nmf_recommender(query,k=10):
    pass

def cos_sim_recommender(query,k=10):
    pass

def popular_recommender(query,k=10):
    pass
