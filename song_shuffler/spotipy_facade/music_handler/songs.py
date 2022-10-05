from typing import List, Dict, Any

from spotipy import Spotify

from song_shuffler.playlist_manipulator.song import Song
from song_shuffler.spotipy_facade.utils import get_all_pages


class SongManager:

    def __init__(self, spotify_obj: Spotify):
        self.spotify = spotify_obj

    def get_song(self, song_uri: str):
        song_detailes = self.spotify.track(song_uri)
        return Song(song_detailes['name'], song_detailes['id'])

    def get_song_uri(self, song_detailes: Dict[str, Any]):
        return song_detailes['id']

    def get_library_liked(self):
        library_song_pager = self.spotify.current_user_saved_tracks()
        all_library_pages = get_all_pages(self.spotify, library_song_pager)
        return [song['track'] for song in all_library_pages]

    def get_feature_analysis(self, song_id: str):
        return self.spotify.audio_analysis(song_id)

    def get_audio_features(self, song_id: str):
        return self.spotify.audio_features(song_id)





