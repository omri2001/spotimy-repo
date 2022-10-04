from spotimy_player import SpotimyPlayer
from spotipy_facade.music_handler.music_manager import MusicManager
from spotipy_facade.scopes.scopes_factory import ScopeFactory
from common.spotify_parsers import REDIRECT_URI
from spotipy_facade.spotimy import Spotimy


class Client(Spotimy):

    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret, REDIRECT_URI, ScopeFactory.all_scopes())
        self.music_manager = MusicManager(self.spotify)
        self.spotimy_player = SpotimyPlayer(self.spotify)

    def add_song(self, song_uri: str):
        song = self.music_manager.get_song(song_uri)
        self.spotimy_player.playlist.add_song(song)

    def add_playlist(self, playlist_uri: str):
        playlist_songs = self.music_manager.get_playlist_songs(playlist_uri)
        self.spotimy_player.playlist.add_songs(playlist_songs)

    def add_album(self, album_uri: str):
        album_songs = self.music_manager.get_album_songs(album_uri)
        self.spotimy_player.playlist.add_songs(album_songs)

