from abc import abstractmethod

from testing.song.song_info import SongInfo


class Feature:

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def calculate(self, song_info: SongInfo) -> float:
        pass
