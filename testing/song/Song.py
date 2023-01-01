from typing import Dict, Union

from testing.features.Feature import Feature
from testing.features.FeatureFactory import FeatureFactory
from testing.song.song_info import SongInfo


class Song:

    def __init__(self, info: SongInfo):
        self.info = info
        self.feature_to_value = self._init_features_empty()

    @property
    def name(self):
        return self.info.name

    def calculate_features(self):
        for feature in self.feature_to_value.keys():
            self.feature_to_value[feature.name] = feature.calculate(self.info)

    def _init_features_empty(self) -> Dict[Feature, float]:
        all_features = FeatureFactory.get_features()
        return {feature: 0 for feature in all_features}
