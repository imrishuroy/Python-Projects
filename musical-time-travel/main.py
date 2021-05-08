from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
print(date)

default_date = "2000-09-05"

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())

all_songs = [song.getText() for song in
             soup.findAll(name="span", class_="chart-element__information__song text--truncate color--primary")]
print(len(all_songs))
print(all_songs)

## Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://sixteenbrains.com",
        client_id="2201fee109eb4fb6a2414cfcef13a595",
        client_secret="fae725d5cd614fadb76ad973a287586a",
        show_dialog=True,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]
song_names = [song.getText() for song in
              soup.findAll(name="span", class_="chart-element__information__song text--truncate color--primary")]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=song_uris)

print(len(song_uris))
