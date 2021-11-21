from flask import Flask
import requests


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World! API em Python!</p>"

@app.route('/movies/<genre>')
def get_movies(genre):
    endpoint = f"https://api.themoviedb.org/3/discover/movie?api_key=d4a0eb627931e1e8dbc864d5afc2202e&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres={genre}&with_watch_monetization_types=flatrate"
    response =  requests.get(endpoint)

    return response.text