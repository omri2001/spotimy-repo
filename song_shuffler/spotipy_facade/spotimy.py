from typing import List

import spotipy as sp

from song_shuffler.spotipy_facade.spotipy_authenticator import SpotipyAuthenticator


class Spotimy:

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str]):
        self.authenticator = SpotipyAuthenticator(client_id, client_secret, redirect_uri, scopes)
        self.spotify = sp.Spotify(auth=self.authenticator.get_token())

    def play(self, device_id: str):
        self.spotify.start_playback(device_id)

    def stop(self, device_id: str):
        self.spotify.pause_playback(device_id)