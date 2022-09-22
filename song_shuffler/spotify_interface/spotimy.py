from typing import List

import spotipy as sp
from tqdm import tqdm
from spotify_interface.spotimy_handler.playlist_handler import PlaylistHandler
from spotify_interface.spotimy_handler.album_handler import AlbumHandler
from spotify_interface.spotimy_handler.song_handler import SongHandler
from spotipy.oauth2 import SpotifyOAuth

class Spotimy:

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, all_scopes: List[str]):
        self.spotify = sp.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                                            redirect_uri=redirect_uri, scope=all_scopes))
        # self.username = ""
        # self.playlist_handler = PlaylistHandler(self, self.username)
        # self.album_handler = AlbumHandler(self)
        # self.song_handler = SongHandler(self)


    #
    # def get_user_name(self):
    #     return self.current_user().display_name
    #
    # def get_user_id(self):
    #     return self.current_user().id
    #
    # def get_all_user_songs(self):
    #     print("getting all user songs...")
    #     all_songs = []
    #     all_songs += self.song_handler.get_library_liked()
    #     for album in tqdm(self.album_handler.get_library_albums()):
    #         all_songs += self.album_handler.get_album_songs(album)
    #     for playlist in tqdm(self.playlist_handler.get_library_playlists()):
    #         all_songs += self.playlist_handler.get_playlist_songs(playlist)
    #     return all_songs

