import requests
import json

TMDB_API_KEY = '9fd49ab00d660f7801565ddb3d5db886'

def get_genre_datas():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(request_url).json()
    # print(genres)
    for genre in genres['genres']:
        # print(genre, type(genre))
        fields = {
            'name': genre['name'],
            }
        data = {
            "model": "movies.genre",
            "pk": genre['id'],
            "fields": fields,
        }

        total_data.append(data)

    with open("./movies/fixtures/movies/genres.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, ensure_ascii=False)

get_genre_datas()