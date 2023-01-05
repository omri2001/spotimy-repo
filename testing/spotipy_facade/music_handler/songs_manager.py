import warnings
from typing import Dict, Any, Optional, Union

from spotipy import Spotify

from testing.song.Song import Song
from testing.song.song_info import SongInfo


class SongManager:

    def __init__(self, spotify_obj: Spotify):
        self.spotify = spotify_obj

    def get_song(self, song_id: str, song_details: Optional[Dict[str, Any]] = None) -> Union[None,Song]:
        if not song_details:
            song_details = self.spotify.track(song_id)
        audio_features = self._get_audio_features(song_id)
        if not audio_features:
            warnings.warn(f"Song: {song_details['name']} doesnt have audio features and thus will not be included in the playlist ")
            return None

        song_info = SongInfo(name=song_details['name'],
                             popularity=song_details['popularity'],
                             danceability=audio_features['danceability'],
                             instrumentalness=audio_features['instrumentalness'],
                             acousticness=audio_features['acousticness'],
                             speechiness=audio_features['speechiness'],
                             duration=audio_features['duration_ms']//60,
                             tempo=audio_features['tempo'],
                             energy=audio_features['energy'],
                             valence=audio_features['valence'],
                             liveness=audio_features['liveness'])
        return Song(song_info)

    def _get_audio_features(self, song_id: str) -> Dict[str, Any]:
        return self.spotify.audio_features(song_id)[0]


