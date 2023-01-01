from dataclasses import asdict

import spotipy as sp

from testing.song.Song import Song
from testing.song.song_info import SongInfo


class SongHandler:

    def __init__(self, sp_obj: sp.Spotify):
        self.sp_obj = sp_obj

    def get_song_by_name(self, song_name: SongInfo.name) -> Song:
        songs_results = self.sp_obj.search(q=f'track:{song_name}', type='track')
        first_song_id = songs_results['tracks']['items'][0]['id']
        return self.get_song_by_id(first_song_id)

    def get_song_by_id(self, song_id: SongInfo.id) -> Song:
        track_info = self._extract_song_info_from_track(song_id)
        features_info = self._extract_song_info_from_features(song_id)
        features_dict = {key: value for key,value in asdict(features_info).items() if value is not None}
        track_dict = {key: value for key,value in asdict(track_info).items() if value is not None}
        song_info = SongInfo(id=song_id, **features_dict, **track_dict)
        return Song(song_info)

    def _extract_song_info_from_track(self, song_id: SongInfo.id) -> SongInfo:
        spotipy_track = self.sp_obj.track(song_id)
        track_info = SongInfo(name=spotipy_track['name'], popularity=spotipy_track['popularity'])
        return track_info

    def _extract_song_info_from_features(self, song_id: SongInfo.id) -> SongInfo:
        audio_features = self.sp_obj.audio_features(song_id)[0]
        features_info = SongInfo(danceability=audio_features['danceability'],
                                 instrumentalness=audio_features['instrumentalness'],
                                 acousticness=audio_features['acousticness'],
                                 speechiness=audio_features['speechiness'],
                                 duration=audio_features['duration_ms']//60,
                                 tempo=audio_features['tempo'],
                                 energy=audio_features['energy'],
                                 valence=audio_features['valence'],
                                 liveness=audio_features['liveness']
                                 )
        return features_info