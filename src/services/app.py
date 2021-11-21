
import requests
import pprint


from requests.models import Response

"""
https://api.themoviedb.org/3/movie/550?api_key=d4a0eb627931e1e8dbc864d5afc2202e

"""

movie_id = 500
api_version = 3
api_key = "d4a0eb627931e1e8dbc864d5afc2202e"
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"

print(api_base_url)


def grab_movie_by_id():
    response = requests.get(endpoint)

    print(response.status_code)
    print(response.text)


def search_movie_by_name():
    movie_id = 500
    api_version = 3
    api_key = "d4a0eb627931e1e8dbc864d5afc2202e"
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/search/movie"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query=Endgame"

    response = requests.get(endpoint)
    
    pprint.pprint(response.json())


def get_genres():
    response = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=d4a0eb627931e1e8dbc864d5afc2202e&language=en-US")
    genres = response.json()

    for i in genres['genres']:
        #print(i)
        print(i['name'])


def get_movie_by_genre(genre):
    response =  requests.get("https://api.themoviedb.org/3/discover/movie?api_key=d4a0eb627931e1e8dbc864d5afc2202e&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=18&with_watch_monetization_types=flatrate")

    movie_list = response.json()
    
    for i in movie_list['results']:
        print (i['id'], i['original_title'])
        print()
        #id
        #image
        #overview
        #title
        #vote average
        #release_date

def get_movie_image():
    movie_id = "502"
    base_image_url = "https://image.tmdb.org/t/p/w500"
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/images?api_key={api_key}&language=en-US&include_image_language=en,null")
    data = response.json()
    
    file_path = data['posters'][0]['file_path']
    
    image_path = base_image_url + file_path
    print(image_path)


    #pprint.pprint(data['posters'][0]['file_path'])



#print(response.text)

#grab_movie_by_id()
#search_movie_by_name()
#get_genres()
#get_movie_by_genre(18)
#get_movie_image() 

