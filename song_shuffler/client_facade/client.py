from typing import List

from spotify_interface.spotimy import Spotimy
from decorator_factory.decorators import handle_invalid_input
import app_interaction_texts
from Iplaylist.playlist import Playlist
from songs_database.song import Song
import tekore as tk

class Client:

    def __init__(self, name: str, client_id: str, client_secret: str):
        redirect_uri = 'http://localhost:8001/redirect/'
        all_scopes = ['playlist-modify-private', 'user-follow-read', 'user-top-read', 'user-read-playback-position',
                      'playlist-read-collaborative', 'user-follow-modify', 'user-read-currently-playing',
                      'user-library-read', 'user-read-private', 'playlist-modify-public', 'user-read-email',
                      'user-read-recently-played', 'playlist-read-private', 'ugc-image-upload',
                      'user-read-playback-state',
                      'user-library-modify', 'user-modify-playback-state']
        self.name = name
        self.spotimy = Spotimy(client_id, client_secret, redirect_uri, all_scopes)
        #self.playlist = Playlist()

    def play(self):
        self.spotimy.spotify.start_playback('9b0b0d5a3cedfa3472ac188773cb3ad73a63b59b')

    def stop(self):
        self.spotimy.spotify.pause_playback('9b0b0d5a3cedfa3472ac188773cb3ad73a63b59b')

    def __hash__(self):
        return self.name

    #
    # def get_name(self):
    #     return self.spotimy.get_user_name()
    #
    # def play_computer(self):
    #     self.spotimy.playback_resume('9b0b0d5a3cedfa3472ac188773cb3ad73a63b59b')
    #
    # def stop_computer(self):
    #     self.spotimy.playback_pause('9b0b0d5a3cedfa3472ac188773cb3ad73a63b59b')









    # def choose_songs(self):
    #     songs_origin_input = input(app_interaction_texts.songs_choose_from)
    #     print(app_interaction_texts.retrive_data)
    #     if songs_origin_input == 'all':
    #         self.playlist.add_songs([Song(song.name, song.id) for song in self.spotimy.get_all_user_songs() if song])
    #     elif songs_origin_input == 'playlist':
    #         self.playlist.add_songs([Song(song.name, song.id) for song in self.get_playlist() if song])
    #
    # def get_playlist(self):
    #     playlist_owner = input(app_interaction_texts.playlist_kind_choose)
    #     if playlist_owner == 'selfmade':
    #         playlists_list = self.spotimy.playlist_handler.get_selfmade_playlists()
    #     elif playlist_owner == 'library':
    #         playlists_list = self.spotimy.playlist_handler.get_library_playlists()
    #     else:
    #         playlists_list = self.spotimy.playlist_handler.get_all_playlists()
    #
    #     playlists_names = self.spotimy.playlist_handler.get_playlists_names(playlists_list)
    #     print(app_interaction_texts.display_playlists_list.format(playlists_names))
    #
    #     playlist_name = input(app_interaction_texts.choose_playlist)
    #     return self.get_playlist_from_name(playlist_name)
    #
    # def get_playlist_songs(self):
    #     return [song.name for song in self.playlist.get_all_songs()]
    #
    # def get_playlist_from_name(self, playlist_name):
    #     playlist = self.spotimy.playlist_handler.get_playlist_from_name(playlist_name)
    #     return self.spotimy.playlist_handler.get_playlist_songs(playlist)
