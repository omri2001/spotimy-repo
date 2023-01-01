from typing import Dict, Union

from testing.features.FeatureFactory import FeatureFactory

save_path = r"C:\Users\USER\Desktop\song_app\song_shuffler\playlist_manipulator\song_save"


class Song:

    def __init__(self, info: Dict[str,Union[str, float]]):
        self.info = info
        self.feature_to_value = self.calculate_features()

    @property
    def name(self):
        return self.info['name']

    def calculate_features(self):
        for feature in self.feature_to_value.keys():
            self.feature_to_value[feature.name] = feature.calculate(self.info)

    def _init_features_empty(self) -> Dict[str, float]:
        all_features = FeatureFactory.get_features()
        return {feature: 0 for feature in all_features}