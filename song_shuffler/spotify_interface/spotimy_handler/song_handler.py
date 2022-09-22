from typing import List

#this class should return the song id or handle single songs
class SongHandler:

    def __init__(self, spotify):
        self.spotify = spotify

    def get_library_liked(self):
        return [song.track for song in self.spotify.all_items(self.spotify.saved_tracks())]

    def get_song_info(self, song_id: str):
        return self.spotify.track(song_id)

    def get_songs_info(self, songs_ids: List[str]):
        return [song for song in self.spotify.tracks(songs_ids)]

    def get_feature_analysis(self, song_id: str):
        return self.spotify.track_audio_analysis(song_id)

    def get_audio_features(self, song_id: str):
        return self.spotify.track_audio_features(song_id)





