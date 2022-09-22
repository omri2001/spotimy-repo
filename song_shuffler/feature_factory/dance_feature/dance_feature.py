from typing import Dict

from feature_factory.feature import Feature
from configs.song_features_config import SONG_DANCE_FEATURE

class DanceFeature(Feature):

    def __init__(self):
        self.name = 'Dance'
        self.weight = 0
        super().__init__(self.name, self.weight)

    def calculate(self, song_features: Dict[str, float]):
        self.weight = song_features[SONG_DANCE_FEATURE]






