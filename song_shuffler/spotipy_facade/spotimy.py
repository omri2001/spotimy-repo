from typing import List

import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

#TODO: need a reinit when token is done
#TODO: init should be on the token not cred and shoulds be another init from credentials


class Spotimy:

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, all_scopes: List[str]):
        self.spotify = sp.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                                            redirect_uri=redirect_uri, scope=all_scopes))

    def play(self, device_id: str):
        self.spotify.start_playback(device_id)

    def stop(self, device_id: str):
        self.spotify.pause_playback(device_id)