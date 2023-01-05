from typing import Literal, List

from testing.Queue import Queue
from testing.song.song_info import SongInfo
from testing.spotipy_facade.spotimy import Spotimy

COMPUTER_ID = "9b0b0d5a3cedfa3472ac188773cb3ad73a63b59b"

class Client:

    def __init__(self):
        self.spotimy = Spotimy()
        self.queue = Queue.init_empty()

    def get_queue(self) -> List[str]:
        return self.queue.song_names

    def load_queue_from_playlist(self, playlist_id: str):
        for song in self.spotimy.music_manager.get_playlist_songs(playlist_id):
            self.queue.add_song(song)

    def add_song_to_queue(self, song_id: SongInfo.id):
        self.queue.add_song(self.spotimy.music_manager.get_song(song_id))

    def shuffle_queue(self, shuffle_type: Literal['random', 'smart']):
        if shuffle_type == 'smart':
            self.queue.smart_shuffle()
        elif shuffle_type == 'random':
            self.queue.random_shuffle()
        else:
            raise Exception(f'invalid shuffle type {shuffle_type}')

    def play_queue(self):
        #load queue
        #start play
        self.spotimy.play(COMPUTER_ID)
    def stop_music(self):
        self.spotimy.stop(COMPUTER_ID)

