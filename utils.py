import requests
from decouple import config
url = "https://api.themoviedb.org/3/movie/popular"

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOGI0ZWFjYTAzNDhjN2IzNjFlNmFiN2Q0YzdjMzEzNCIsInN1YiI6IjY0NjdkNTFmYTRhZjhmMDBlNDRiYmQxNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1-ldwiCtuwEXBKcllfcWRkLFJeVylQMF0YiRTS27v3s"
# }

# response = requests.get(url, headers=headers)

# print(response.text)

my_key = config("MY_TMDB_API_KEY")

def get_movie_data(url):
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {my_key}"
}
    coins = requests.get(url, headers=headers)
    jsonified = coins.json()
    return jsonified

print(get_movie_data(url))

