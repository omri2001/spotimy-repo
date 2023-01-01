from typing import Literal, List

from testing.Queue import Queue
from testing.song.song_info import SongInfo
from testing.spotimy.handlers.music_handler import MusicHandler


class Client:

    def __init__(self):
        self.music_handler = MusicHandler()
        self.queue = Queue.init_empty()

    def get_queue(self) -> List[str]:
        return self.queue.song_names

    def load_queue_from_playlist(self, playlist_id: str):
        for song in self.music_handler.get_playlist_songs_from_id(playlist_id):
            self.queue.add_song(song)

    def add_song_to_queue(self, song_id: SongInfo.id):
        self.queue.add_song(self.music_handler.get_song_by_id(song_id))

    def shuffle_queue(self, shuffle_type: Literal['random', 'smart']):
        if shuffle_type == 'smart':
            self.queue.smart_shuffle()
        elif shuffle_type == 'random':
            self.queue.random_shuffle()
        else:
            raise Exception(f'invalid shuffle type {shuffle_type}')

    def play_queue(self):
        pass
    def stop_music(self):
        pass

