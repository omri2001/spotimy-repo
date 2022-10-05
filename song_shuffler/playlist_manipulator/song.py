from typing import Dict
import pickle
from os import listdir

from song_shuffler.feature_factory.feature import Feature
from song_shuffler.feature_factory.feature_factory import FeatureFactory

save_path = r"C:\Users\USER\Desktop\song_app\song_shuffler\playlist_manipulator\song_save"


class Song:

    def __init__(self, name: str, id: str):
        self.name: str = name
        self.id: str = id
        self.features: Dict[str, Feature] = self._init_features()

    def create_features(self, audio_features):
        features = audio_features.asbuiltin()
        return features

    def get_feature(self, feature_name):
        return self.features[feature_name]

    def set_feature_weight(self, feature_name, feature_weight):
        self.features[feature_name].re_evaluate(feature_weight)

    def calculate_features(self):
        self.features = {feature_name: feature.calculate() for feature_name, feature in self.features.items()}

    def save_song(self):
        with open(f'{save_path}/{self.id}', 'wb') as fout:
            pickle.dump([feature for feature in self.features], fout)

    def _init_features(self) -> Dict[str, Feature]:
        if self._is_song_exist():
            return self._load_features()
        return {feature.name: feature for feature in FeatureFactory.get_features()}

    def _is_song_exist(self) -> bool:
        return self.id in listdir(save_path)

    def _load_features(self) -> Dict[str, Feature]:
        with open(f'{save_path}/{self.id}', 'rb') as fp:
            loaded_features = pickle.load(fp)
        loaded_features = {feature.name: feature for feature in loaded_features}
        new_features = {feature.name: feature for feature in FeatureFactory.get_features()}
        loaded_features.update(new_features)
        return loaded_features
