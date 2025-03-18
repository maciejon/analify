import requests
import json
import os
import handle_request as hr

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

r = requests.post('https://accounts.spotify.com/api/token', headers={'Content-Type': 'application/x-www-form-urlencoded'}, data = f'grant_type=client_credentials&client_id={SPOTIFY_CLIENT_ID}&client_secret={SPOTIFY_CLIENT_SECRET}').json()

print(r)
access_token = r['access_token']

print(access_token)

artist = requests.get('https://api.spotify.com/v1/artists/699OTQXzgjhIYAHMy9RyPD?si=5741889096a64a83', headers={'Authorization': f'Bearer {access_token}'})
print(artist.content)

artist = hr.handle_request(url='https://api.spotify.com/v1/artists/699OTQXzgjhIYAHMy9RyPD?si=5741889096a64a83', type='GET', headers={'Authorization': f'Bearer {access_token}'})
print(artist.content)

print(hr.handle_request(url='https://api.spotify.com/v1/me',type='GET',headers={'Authorization': f'Bearer {access_token}'}).content())