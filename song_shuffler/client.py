from spotipy_facade.music_handler.music_manager import MusicManager
from spotipy_facade.scopes.scopes_factory import ScopeFactory
from common.spotify_parsers import REDIRECT_URI, COMPUTER_ID
from spotipy_facade.spotimy import Spotimy


class Client:

    def __init__(self, name: str, client_id: str, client_secret: str):
        self.name = name
        self.spotimy = Spotimy(client_id, client_secret, REDIRECT_URI, ScopeFactory.all_scopes())
        self.music_manager = MusicManager(self.spotimy.spotify)

    def play(self):
        self.spotimy.play(COMPUTER_ID)

    def stop(self):
        self.spotimy.stop(COMPUTER_ID)
