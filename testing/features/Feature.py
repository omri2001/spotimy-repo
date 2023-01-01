from abc import abstractmethod
from typing import Dict, Union


class Feature:

    @abstractmethod
    @property
    def name(self) -> str:
        pass

    @abstractmethod
    def calculate(self, song_info: Dict[str, Union[str, float]]) -> float:
        pass
