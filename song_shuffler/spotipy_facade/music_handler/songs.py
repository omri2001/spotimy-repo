from typing import List

from spotipy import Spotify

from spotipy_facade.utils import get_all_pages


class SongManager:

    def __init__(self, spotify_obj: Spotify):
        self.spotify = spotify_obj

    def get_library_liked(self):
        library_song_pager = self.spotify.current_user_saved_tracks()
        all_library_pages = get_all_pages(self.spotify, library_song_pager)
        return [song['track'] for song in all_library_pages]

    def get_song_info(self, song_id: str):
        return self.spotify.track(song_id)

    def get_songs_info(self, songs_ids: List[str]):
        return [song for song in self.spotify.tracks(songs_ids)]

    def get_feature_analysis(self, song_id: str):
        return self.spotify.audio_analysis(song_id)

    def get_audio_features(self, song_id: str):
        return self.spotify.audio_features(song_id)





