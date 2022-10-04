from typing import List

import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth


class Spotimy:

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str]):
        token = self._get_spotify_token(client_id, client_secret, redirect_uri, scopes)
        self.spotify = sp.Spotify(auth=token)

    def _get_spotify_token(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str]):
        oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret,redirect_uri=redirect_uri, scope=scopes)
        token = oauth.get_access_token()
        return token['access_token']

    def play(self, device_id: str):
        self.spotify.start_playback(device_id)

    def stop(self, device_id: str):
        self.spotify.pause_playback(device_id)