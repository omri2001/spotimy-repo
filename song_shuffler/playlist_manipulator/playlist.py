import random
from typing import List

from song_shuffler.playlist_manipulator.song import Song
from song_shuffler.playlist_manipulator.song_list import SongList


class Playlist:

    def __init__(self, songs: List[Song]):
        self.unplayed = SongList(songs)
        self.played = SongList.init_empty()

    @classmethod
    def init_empty(cls):
        return cls([])

    @property
    def empty(self):
        return len(self.unplayed) == 0

    def add_song(self, song: Song):
        self.unplayed.add(song)

    def add_songs(self, songs: List[Song]):
        self.unplayed.add(songs)

    def normalize(self):
        # needs to be all weights
        self.unplayed.normalize_weights()

    def play_song(self):
        # maybe problem is you can ad a song to be next but never play it but itll be like it played
        song = self.unplayed[0]
        self.unplayed.remove(song)
        self.played.add(song)
        return song

    def played(self, song: Song):
        self.unplayed.remove(song)
        self.played.add(song)

    def random_shuffle(self):
        random.shuffle(self.unplayed.songs)

    def reset_playlist(self):
        self.unplayed = SongList(self.unplayed.songs() + self.played.songs())
        self.played = SongList.init_empty()

    def get_all_songs(self) -> List[Song]:
        return self.unplayed + self.played()

    def __iter__(self):
        return self

    def __next__(self):
        if self.unplayed:
            return self.play_song()
        else:
            raise StopIteration

    def __getitem__(self, slice_obj):
        if isinstance(slice_obj, int):
            return self.unplayed[slice_obj]
        start, stop, step = slice_obj.start, slice_obj.stop, slice_obj.step
        if not start:
            start = 0
        if not stop:
            step = 1
        if not step:
            stop = len(self.unplayed)
        return self.unplayed[start:stop:step]

    def __len__(self):
        return len(self.unplayed)