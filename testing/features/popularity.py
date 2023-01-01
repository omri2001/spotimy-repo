from typing import Dict, Union

from testing.features.Feature import Feature
from testing.song.song_info import SongInfo


class Popularity(Feature):
    @property
    def name(self) -> str:
        return "Popularity"

    def calculate(self, song_info: SongInfo) -> float:
        return song_info.popularity