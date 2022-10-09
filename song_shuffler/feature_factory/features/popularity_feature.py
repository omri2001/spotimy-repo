from typing import Dict

from song_shuffler.feature_factory.feature import Feature

POPULARITY_FEATURE = 'popularity'

class Popularity(Feature):

    def __init__(self):
        self.name = 'Popularity'
        self.weight = 0
        super().__init__(self.name, self.weight)

    def calculate(self, song_features: Dict[str, str]):
        self.weight = song_features[POPULARITY_FEATURE]




