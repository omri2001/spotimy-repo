from typing import Dict, Union

from testing.features.Feature import Feature


class Danceability(Feature):

    @property
    def name(self) -> str:
        return "Danceability"

    def calculate(self, song_info: Dict[str, Union[str, float]]):
        pass