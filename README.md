# Time Travel Spotify Playlist

## Overview
A Python project that creates Spotify playlists from the Billboard Hot 100 chart of any date you choose. By scraping Billboard’s website for track titles and integrating with Spotify’s API, the program automatically builds a private playlist on your account filled with the top hits of that day.

## Features
- Input any date (`YYYY-MM-DD`) to fetch Billboard Hot 100.
- Scrapes song titles with BeautifulSoup.
- Authenticates with Spotify using Spotipy and OAuth.
- Searches tracks on Spotify and collects their URIs.
- Creates a private playlist in your account with the songs.
- Playlist is named with the chosen date plus a custom label.

## Requirements
- Python 3.10+
- Spotify Developer account & app credentials
- `.env` file containing:<br>
CLIENT_ID=your_spotify_client_id<br>
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URL=http://localhost:8888/callback
AGENT=Mozilla/5.0
