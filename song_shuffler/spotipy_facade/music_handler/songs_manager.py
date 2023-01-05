from typing import Dict, Any

from spotipy import Spotify

from song_shuffler.playlist_manipulator.song import Song
from testing.spotipy_facade.utils import get_all_pages

EMPTY_SONG_AUDIO_FEATURES = {'danceability': 0.0001, 'energy': 0.0001, 'key': 0.0001, 'loudness': 0.0001, 'mode': 0.0001,
                             'speechiness': 0.0001, 'acousticness': 0.0001, 'instrumentalness': 0.0001, 'liveness': 0.0001,
                             'valence': 0.0001, 'tempo': 0.0001, 'duration_ms': 0.0001, 'time_signature': 0.0001}

class SongManager:

    def __init__(self, spotify_obj: Spotify):
        self.spotify = spotify_obj

    def get_song(self, song_uri: str):
        song_detailes = self.spotify.track(song_uri)
        song_audio_features = self.spotify.audio_features(song_uri)[0]
        if song_audio_features == None:
            song_audio_features = EMPTY_SONG_AUDIO_FEATURES
        song_audio_features.update({'popularity': song_detailes['popularity']/100})
        return Song(song_detailes['name'], song_detailes['id'], song_audio_features)

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





