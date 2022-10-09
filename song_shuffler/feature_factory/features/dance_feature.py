from typing import Dict

from song_shuffler.feature_factory.feature import Feature

SONG_DANCE_FEATURE = 'danceability'

class DanceFeature(Feature):

    def __init__(self):
        self.name = 'Dance'
        self.weight = 0
        super().__init__(self.name, self.weight)

    def calculate(self, song_features: Dict[str, str]):
        self.weight = song_features[SONG_DANCE_FEATURE]




