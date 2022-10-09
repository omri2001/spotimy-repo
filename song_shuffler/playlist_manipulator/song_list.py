from __future__ import annotations
from typing import List, Union, Dict

from song_shuffler.playlist_manipulator.song import Song


class SongList:

    def __init__(self, songs: List[Song]):
        self.songs = songs

    @classmethod
    def init_empty(cls):
        return cls([])

    def re_order_by_weights(self, features_weights: Dict[str,float]):
        features_weights = self._normalize_weights(features_weights)
        for song in self.songs:
            song.recalculate_song_score(features_weights)
        self.songs = sorted(self.songs, key=lambda song: song.score)

    def _normalize_weights(self, features_weights: Dict[str,float]) -> Dict[str, float]:
        max_weight = max(features_weights.values())
        return {feature_name: weight/max_weight for feature_name, weight in features_weights.items()}

    def add(self, songs: Union[Song, List[Song]]):
        if isinstance(songs, list):
            self.songs += songs
        else:
            self.songs.append(songs)

    def remove(self, songs: Union[Song, List[Song]]):
        if not isinstance(songs, list):
            songs = [songs]
        for song in songs:
            self.songs.remove(song)

    def __getitem__(self, slice_obj):
        if isinstance(slice_obj, int):
            return self.songs[slice_obj]
        start, stop, step = slice_obj.start, slice_obj.stop, slice_obj.step
        if not start:
            start = 0
        if not stop:
            step = 1
        if not step:
            stop = len(self.songs)
        return self.songs[start:stop:step]

    def __len__(self):
        return len(self.songs)