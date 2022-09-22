import random
from typing import List

from playlist_manipulator.song import Song
from playlist_manipulator.song_list import SongList


class Playlist:

    def __init__(self, songs: List[Song]):
        self.unplayed = SongList(songs)
        self.unplayed.calculate_songs_features()
        self.played = SongList.init_empty()

    def add_song(self, songs: List[Song]):
        self.unplayed.add(songs)

    def add_songs(self, songs: List[Song]):
        self.unplayed.add(songs)

    def normalize(self):
        #needs to be all weights
        self.unplayed.normalize_weights()

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
