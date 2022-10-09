from typing import List

from spotipy import Spotify

from song_shuffler.playlist_manipulator.song import Song
from song_shuffler.spotipy_facade.music_handler.songs import SongManager
from song_shuffler.spotipy_facade.utils import get_all_pages


class PlaylistManager:

    def __init__(self, spotify_obj: Spotify):
        self.spotify = spotify_obj
        self.song_manager = SongManager(self.spotify)
        self.username = spotify_obj.current_user()['id']

    def get_playlist_songs(self, playlist_uri: str) -> List[Song]:
        playlist_pager = self.spotify.playlist_items(playlist_uri)
        return [self.song_manager.get_song(song['track']['id']) for song in get_all_pages(self.spotify, playlist_pager)]
    #
    # def get_all_playlists(self):
    #     return [playlist for playlist in self.spotify.all_items(self.spotify.playlists(self.username))]
    #
    # def get_selfmade_playlists(self):
    #     return [playlist for playlist in self.get_all_playlists() if playlist.owner.id == self.username]
    #
    # def get_library_playlists(self):
    #     all_playlists = self.get_all_playlists()
    #     return [playlist_info for playlist_info in all_playlists if playlist_info.owner.id != self.username]
    #
    # def get_playlist_id(self, playlist):
    #     return playlist.id
    #
    # def get_playlist_name(self, playlist):
    #     return self.spotify.playlist(playlist.id).name
    #
    # def get_playlists_names(self, playlists):
    #     return [self.get_playlist_name(playlist) for playlist in playlists]
    #
    # def get_playlist_from_name(self, playlist_name):
    #     all_playlist = self.get_all_playlists()
    #     playlist = [playlist for playlist in all_playlist if self.get_playlist_name(playlist) == playlist_name]
    #     if len(playlist) >= 1:
    #         return playlist[0]
    #     else:
    #         print("wrong playlist name, playlist name not in list")