from flask import Flask
import requests


app = Flask(__name__)

api_base_url = f"https://api.themoviedb.org/3/"
api_key = "d4a0eb627931e1e8dbc864d5afc2202"
endpoint_path = "discover/movie?"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
@app.route("/")
def hello_world():
    return "<p>Bem vindo! API em Flask!</p>"

@app.route('/movies/<genre>')
def get_movies(genre):
    endpoint = f"{api_base_url}{endpoint_path}api_key={api_key}e&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres={genre}&with_watch_monetization_types=flatrate"
    response =  requests.get(endpoint)

    return response.text

