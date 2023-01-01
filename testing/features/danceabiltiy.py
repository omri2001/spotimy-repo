from typing import Dict, Union

from testing.features.Feature import Feature
from testing.song.song_info import SongInfo


class Danceability(Feature):

    @property
    def name(self) -> str:
        return "Danceability"

    def calculate(self, song_info: SongInfo):
        return song_info.danceability