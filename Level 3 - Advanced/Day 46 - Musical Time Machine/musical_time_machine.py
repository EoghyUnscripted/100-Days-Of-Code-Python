"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 46
PROJECT: Musical Time Machine
LEVEL: Advanced

"""

from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup


# Billboard Hot 100 URL prefix
billboard = "https://www.billboard.com/charts/hot-100/"

# Get user input to pull the Billboard Hot 100 from the past
date = input("Let's visit the musical past. Type in a year and let's do the time warp! [YYYY-MM-DD]: ")
billboard += date

r = requests.get(billboard)     # Get website data

bt100_html = r.text     # Get the returned text as HTML

soup = BeautifulSoup(bt100_html, "html.parser")     # Create Beautiful Soup class object

get_titles = soup.select("li h3")       # Find the song titles

song_titles = [get_titles[num].getText().strip() for num in range(0,100)]       # Append first 100 results to list and clean strings

# Spotipy Authentication
spot = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=config("SPOTIFY_ID"),
        client_secret=config("SPOTIFY_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)

"""

    The following code was copied from the project solution as the Spotipy documentation did not provide
    the necessary information to perform the tasks assigned in obtaining the Spotify URI's for tracks,
    which is necessary for adding tracks to a new playlist.
    
"""

user_id = spot.current_user()["id"]     # Get current username

song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = spot.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
playlist = spot.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

spot.playlist_add_items(playlist_id=playlist["id"], items=song_uris)