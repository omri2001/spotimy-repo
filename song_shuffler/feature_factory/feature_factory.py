from feature_factory.dance_feature.dance_feature import DanceFeature


FEATURES_NAMES = ['chill', 'hype', 'rap', 'french', 'hebrew', 'live']

class FeatureFactory:

    @staticmethod
    def get_features():
        return [DanceFeature()
                ]

    @staticmethod
    def get_feature_from_name(feature_name):
        if feature_name == 'Dance':
            return DanceFeature()