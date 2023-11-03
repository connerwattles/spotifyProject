import spotipy;
from spotipy.oauth2 import SpotifyClientCredentials;

SPOTIFY_CLIENT_ID = "8561f34555a14d9099db8509edfe7339";
SPOTIFY_CLIENT_SECRET = "f0f1379757d64bb299d572313c2961f7";


# Path: config.py
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
pmt_uri = 'spotify:show:5ss1pqMFqWjkOpt6Ag0fZW'
cwatts_uri = 'spotify:user:31mwgetts7mfg6gyqqaboejnrrz4'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))


##Birdy albums
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

##PMT episodes

'''
results = spotify.show_episodes(pmt_uri, limit = 50)
episodes = results['items']
for i in range(10):
    results = spotify.next(results)
    episodes.extend(results['items'])

for episode in episodes:
    print(episode['name'])
    '''

##Conner's Playlists
print("Conner's Playlists:")

restult = spotify.user_playlists()
results = spotify.user_playlists(cwatts_uri)
playlists = results['items']
while results['next']:
    results = spotify.next(results)
    playlists.extend(results['items'])

for playlist in playlists:
    print(playlist['name'])
