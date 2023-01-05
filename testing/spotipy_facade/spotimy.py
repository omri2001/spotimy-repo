import spotipy as sp

from testing.spotipy_facade.music_handler.music_manager import MusicManager
from testing.spotipy_facade.spotipy_authenticator import SpotipyAuthenticator


class Spotimy:

    def __init__(self):
        self.authenticator = SpotipyAuthenticator()
        self.spotify = sp.Spotify(auth=self.authenticator.get_token())

        self.music_manager = MusicManager(self.spotify)


    def play(self, device_id: str):
        self.spotify.start_playback(device_id)

    def stop(self, device_id: str):
        self.spotify.pause_playback(device_id)