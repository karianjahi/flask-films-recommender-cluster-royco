from flask import Flask
from flask import render_template
from flask import request
from simple_recommender import get_recommendation
from utils import movies, list2dict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           title="Hello cluster roycos!!",
                           movies=movies)

@app.route('/recommender')
def recommender():
    method = request.args.getlist("method")
    movies = request.args.getlist("movie")
    ratings = request.args.getlist("rating")
    user_dict = list2dict(movies, ratings)
    print(user_dict)
    recs = get_recommendation()
    return render_template('recommendations.html', selected_movies=recs)


if __name__=="__main__":
    app.run(debug=True, port=5001)