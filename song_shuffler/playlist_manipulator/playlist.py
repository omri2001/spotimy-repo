import random
from typing import List

from playlist_manipulator.song import Song
from playlist_manipulator.song_list import SongList


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
        #needs to be all weights
        self.unplayed.normalize_weights()

    def play_song(self):
        #maybe problem is you can ad a song to be next but never play it but itll be like it played
        song = self.unplayed[0]
        self.unplayed.remove(song)
        self.played.add(song)
        return song

    def played(self, song: Song):
        self.unplayed.remove(song)
        self.played.add(song)

    def random_shuffle(self):
        random.shuffle(self.unplayed)

    def reset_playlist(self):
        self.unplayed = SongList(self.unplayed.songs() + self.played.songs())
        self.played = SongList.init_empty()

    def get_all_songs(self) -> List[Song]:
        return self.unplayed + self.played()
