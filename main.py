import os
import spotipy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

date : str = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
header : dict[str, str] = {
    "User-Agent": os.environ.get("AGENT")
}

response = requests.get(url, headers=header)
content = response.text

soup = BeautifulSoup(content, "html.parser")
titles = [title.get_text(strip=True) for title in soup.select("li.o-chart-results-list__item h3")]
print(titles)

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET"),
    redirect_uri=os.environ.get("REDIRECT_URL"),
    scope="playlist-modify-private")
)
user_id = spotify.current_user()["id"]

def create_playlist(user: str, date_time: str) -> str:
    playlist_name : str = date_time + " " + input("Enter playlist title: ")
    playlist = spotify.user_playlist_create(user=user, name=playlist_name, public=False)
    return playlist["id"]

def find_track_uri(track_title: str, date_time: str) -> str | None:
    query = f"track:\"{track_title}\" year:1960-{date_time.split('-')[0]}"
    result = spotify.search(q=query, type="track", limit=1)
    if result["tracks"]["total"] > 0:
        return result["tracks"]["items"][0]["uri"]
    else:
        return None

spotify_uri = [uri for uri in (find_track_uri(title, date) for title in titles) if uri]
print(spotify_uri)

playlist_id = create_playlist(user_id, date)
spotify.playlist_add_items(playlist_id=playlist_id, items=spotify_uri)