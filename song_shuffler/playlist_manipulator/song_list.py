from __future__ import annotations
from typing import List, Union

from playlist_manipulator.song import Song



class SongList:

    def __init__(self, songs: List[Song]):
        self.songs = songs

    @classmethod
    def init_empty(cls):
        return cls([])

    def calculate_songs_features(self):
        [song.calculate_features() for song in self.songs]

    def normalize_weights(self, feature_name):
        max_feature_weight = max(song.get_feature(feature_name) for song in self.songs)
        [song.set_feature_weight(feature_name, song.features[feature_name] / max_feature_weight) for song in self.songs]

    def add(self, songs: Union[Song, List[Song]]):
        if isinstance(songs, list):
            self.songs += songs
        else:
            self.songs.append(songs)

    def remove(self, songs: Union[Song, List[Song]]):
        if not isinstance(songs, list):
            songs = [songs]
        for song in songs:
            self.songs.remove(song)

    def __getitem__(self, item):
        return self.songs[item]

    def __len__(self):
        return len(self.songs)