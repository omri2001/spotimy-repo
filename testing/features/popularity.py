from typing import Dict, Union

from testing.features.Feature import Feature


class Popularity(Feature):
    @property
    def name(self) -> str:
        return "Popularity"

    def calculate(self, song_info: Dict[str, Union[str, float]]) -> float:
        return song_info['popularity']