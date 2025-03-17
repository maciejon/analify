import requests
import json
import os

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

r = requests.post('https://accounts.spotify.com/api/token', headers={'Content-Type': 'application/x-www-form-urlencoded'}, data = f'grant_type=client_credentials&client_id={SPOTIFY_CLIENT_ID}&client_secret={SPOTIFY_CLIENT_SECRET}').json()

print(r)
access_token = r['access_token']

print(access_token)

artist = requests.get('https://api.spotify.com/v1/artists/699OTQXzgjhIYAHMy9RyPD?si=5741889096a64a83', headers={'Authorization': f'Bearer {access_token}'})
print(artist.content)

def handle_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        print("Success, code:", response.status_code)
    else:
        raise Exception("Fail, code:", response.status_code)

    print(response.headers["Content-Type"])

    response_dict = response.json()

# handle_request()