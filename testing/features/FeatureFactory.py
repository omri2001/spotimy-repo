from typing import List

from testing.features.Feature import Feature
from testing.features.danceabiltiy import Danceability
from testing.features.popularity import Popularity


class FeatureFactory:

    @staticmethod
    def get_features() -> List[Feature]:
        return [Danceability(), Popularity()]

    @staticmethod
    def get_feature_from_name(feature_name) -> Feature:
        for feature in FeatureFactory.get_features():
            if feature.name == feature_name:
                return feature
        raise Exception(f"No such feature exists, with feature name: {feature_name}")

    @staticmethod
    def get_features_names() -> List[str]:
        return [feature.name for feature in FeatureFactory.get_features()]