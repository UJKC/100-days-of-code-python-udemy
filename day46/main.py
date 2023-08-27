import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

year = input("Enter the year you want to scrape (1990, 2000): ")
month = input("Enter the month you want to scrape (05, 12): ")
date = input("Enter the date you want to scrape (5, 15): ")

URL = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{date}/"

response = requests.get(URL)
ujwal = response.text

Soup = BeautifulSoup(ujwal, "lxml")
songlist = Soup.select("li ul li h3")
songs_list_text = []

for music in songlist:
    songs_list_text.append(music.getText().strip())

print(songs_list_text)



# Replace with your own credentials and redirect URI
client_id = ""
client_secret = ""
redirect_uri = "https://localhost:3000"  # Make sure this matches your app's settings

# Initialize the SpotifyOAuth object
sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope="playlist-modify-private playlist-read-private")

# Get the authorization URL
auth_url = sp_oauth.get_authorize_url()

# Print the URL and ask the user to copy and paste it in a browser
print(f"Please visit this URL to authorize your Spotify account: {auth_url}")

# After authorizing, get the token using the URL from the redirected page
response_url = input("Paste the redirected URL here: ")
token_info = sp_oauth.get_access_token(response_url)

# Initialize Spotipy with the obtained token
sp = spotipy.Spotify(auth=token_info['access_token'])

# Now you can use Spotipy to make API calls
user_info = sp.current_user()
print("Logged in as:", user_info['display_name'])

trackuri = []
for song_name in songs_list_text:

    try:
        # Search for the song
        results = sp.search(q=song_name, type="track")

        # Get the first track from the search results
        if results["tracks"]["items"]:
            track = results["tracks"]["items"][0]
            track_name = track["name"]
            track_uri = track["uri"]
            print(f"Track found: {track_name}\nTrack URI: {track_uri}")
            trackuri.append(track_uri)
        else:
            print("Song not found on Spotify.")

    except spotipy.exceptions.SpotifyException as e:
        print("An error occurred:", e)

print(trackuri)

playlist_name = f"{year}-{month}-{date}"
playlist_description = "A playlist created using Spotipy"
user_id = sp.me()['id']

playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description=playlist_description)

print("New playlist created:")
print("Playlist Name:", playlist['name'])
print("Playlist ID:", playlist['id'])

# Add tracks to the playlist
sp.playlist_add_items(playlist['id'], trackuri)

print("Songs added to the playlist:", playlist_name)