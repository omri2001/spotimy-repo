from typing import List

from song_shuffler.feature_factory.feature_factory import FeatureFactory
from song_shuffler.playlist_manipulator.song import Song


class Queue:

    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.feature_name_to_weights = {feature_name: 100 for feature_name in FeatureFactory.get_features_names()}

    def smart_shuffle(self):
        pass
    def random_shuffle(self):
        pass
    def add_song(self):
        pass
    def remove_song(self):
        pass