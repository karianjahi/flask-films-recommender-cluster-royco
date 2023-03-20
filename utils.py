movies = [f'film{i}' for i in range(1, 51)]


def list2dict(movies: list, ratings: list):
    movie_ratings_dict = {}
    for movie, rating in zip(movies, ratings):
        movie_ratings_dict[movie] = rating
    return movie_ratings_dict

if __name__ == "__main__":
    movies = ["flight", "disgruntled"]
    ratings = [2, 5]
    print(list2dict(movies, ratings))



