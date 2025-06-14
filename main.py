import webbrowser
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope='user-library-read'
))

results = sp.current_user_saved_tracks(limit=50, offset=0)
total = results['total']
all_links = []

for offset in range(0, total, 50):
    results = sp.current_user_saved_tracks(limit=50, offset=offset)
    for item in results['items']:
        track_url = item['track']['external_urls']['spotify']
        all_links.append(track_url)

print(" Playing a random song from your liked tracks...")
random_link = random.choice(all_links)
webbrowser.open(random_link)
