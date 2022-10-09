from typing import List

from song_shuffler.feature_factory.feature import Feature
from song_shuffler.feature_factory.features.dance_feature import DanceFeature
from song_shuffler.feature_factory.features.popularity_feature import Popularity


class FeatureFactory:

    @staticmethod
    def get_features() -> List[Feature]:
        return [DanceFeature(),
                Popularity()
                ]

    @staticmethod
    def get_feature_from_name(feature_name) -> Feature:
        if feature_name == 'Dance':
            return DanceFeature()
        elif feature_name == 'Popularity':
            return Popularity()

    @staticmethod
    def get_features_names() -> List[str]:
        return [feature.name for feature in FeatureFactory.get_features()]