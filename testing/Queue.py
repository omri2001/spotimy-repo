import random
from typing import List

from testing.features.FeatureFactory import FeatureFactory
from testing.song.Song import Song


class Queue:

    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.feature_name_to_weights = {feature_name: 100 for feature_name in FeatureFactory.get_features_names()}

    @classmethod
    def init_empty(cls):
        return cls([])
    @property
    def song_names(self) -> List[str]:
        return [song.name for song in self.songs]
    def add_song(self, song: Song):
        self.songs.append(song)
    def smart_shuffle(self):
        raise NotImplementedError
    def random_shuffle(self):
        random.shuffle(self.songs)

