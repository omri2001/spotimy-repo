import random
from typing import List

from songs_database.song import Song
from Iplaylist.song_list import SongList


class Playlist:

    def __init__(self):
        self.unplayed = SongList.init_empty()
        self.played = SongList.init_empty()

    def add_song(self, song: Song):
        self.unplayed.add_songs(song)

    def add_songs(self, songs: List[Song]):
        self.unplayed.add_songs(songs)

    def normalize(self):
        self.unplayed.normalize_weights()

    def calculate(self):
        self.unplayed.calculate_songs_features()

    def played(self, song: Song):
        self.unplayed.remove_song(song)
        self.played.add_song(song)

    def random_shuffle(self):
        self.unplayed.shuffle()

    def reset_playlist(self):
        self.unplayed = SongList(self.unplayed.get_songs() + self.played.get_songs())
        self.played = SongList.init_empty()

    def get_all_songs(self):
        return self.unplayed + self.played
