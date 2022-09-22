import random
from typing import List
from songs_database.song import Song

# probably should inherit form List


class SongList:

    def __init__(self, songs: List[Song]):
        self.songs = songs

    @classmethod
    def init_empty(cls):
        return cls([])

    def calculate_songs_features(self):
        [song.calculate_features() for song in self.songs]

    def normalize_weights(self, feature_name):
        max_feature_weight = self.get_max_feature_weight(feature_name)
        [song.set_feature_weight(feature_name, song.features[feature_name] / max_feature_weight) for song in self.songs]

    def get_max_feature_weight(self, feature_name):
        return max(song.get_feature(feature_name) for song in self.songs)

    def get_min_feature_weight(self, feature_name):
        return min(song.get_feature(feature_name) for song in self.songs)

    def get_all_songs_feature_weights(self, feature_name):
        return [song.get_feature(feature_name) for song in self.songs]

    def get_songs(self):
        return self.songs

    def add_song(self, song: Song):
        self.songs.append(song)

    def add_songs(self, songs: List[Song]):
        self.songs += songs

    def remove_song(self, song):
        self.songs.remove(song)

    def shuffle(self):
        random.shuffle(self.songs)

    def __add__(self, other_songs):
        return self.get_songs() + other_songs.get_songs()

