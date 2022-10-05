import time
from typing import List

from spotipy import Spotify

from song_shuffler.playlist_manipulator.playlist import Playlist
from song_shuffler.common.spotify_parsers import COMPUTER_ID

MEGAN_BITCH_SONG = '06scTb0zbkxYNgpAB3J9fN'
NEVERITA_SONG = '31i56LZnwE6uSu3exoHjtB'
DEECIEN_SONG = '50jULvLQIKWfZWGIh3rYEd'

class SpotimyPlayer:

    def __init__(self, spotify_obj: Spotify):
        self.spotify = spotify_obj
        self.playlist = Playlist.init_empty()
        self.playing = False

    def start_playback(self, num_of_songs: int = None):
        assert not self.playlist.empty
        self.playing = True
        print("shuffeling")
        self.playlist.random_shuffle()

        print("loading first track")
        self._load_first_track()
        self.load_queue(num_of_songs=num_of_songs-1)

    def _load_first_track(self):
        self.clear_queue()
        self.spotify.volume(0, COMPUTER_ID)
        self.spotify.start_playback(COMPUTER_ID)
        first_song = self.playlist.play_song()
        self.spotify.add_to_queue(first_song.id)
        self.spotify.next_track(COMPUTER_ID)
        self.spotify.volume(100, COMPUTER_ID)

    def load_queue(self, num_of_songs: int = None, reset_queue: bool = False):
        print("loading queue")
        num_of_songs = len(self.playlist) if not num_of_songs else num_of_songs
        if self._is_playing():
            for index, song in enumerate(self.playlist):
                if index == num_of_songs:
                    break
                self.spotify.add_to_queue(song.id, COMPUTER_ID)
        else:
            self.spotify.volume(0, COMPUTER_ID)
            self.play()
            if reset_queue:
                self._add_songs_to_queue([NEVERITA_SONG, NEVERITA_SONG, NEVERITA_SONG, NEVERITA_SONG, MEGAN_BITCH_SONG])
                self.load_queue(num_of_songs=num_of_songs, reset_queue=reset_queue)
                self._clear_queue_till(MEGAN_BITCH_SONG)
            else:
                self.load_queue(num_of_songs=num_of_songs, reset_queue=reset_queue)
            self.stop()
            self.spotify.volume(100, COMPUTER_ID)
        print("done loading")

    def _add_songs_to_queue(self, songs_ids: List[str]):
        for song in songs_ids:
            self.spotify.add_to_queue(song)

    def _clear_queue_till(self, song_id: str):
        current_song_id = self.spotify.current_playback()['item']['id']
        while current_song_id != song_id:
            self.spotify.next_track()
            time.sleep(0.01)
            current_song_id = self.spotify.current_playback()['item']['id']

    def _is_playing(self):
        playing = self.spotify.current_user_playing_track()
        if playing:
            return playing['is_playing']
        return False

    def stop(self):
        assert self._is_playing()
        self.spotify.pause_playback(COMPUTER_ID)
        self.playing = False
        time.sleep(2)

    def play(self):
        assert not self._is_playing()
        self.spotify.start_playback(COMPUTER_ID)
        self.playing = True
        time.sleep(2)

    def clear_queue(self, way: str = None):
        print("clearing queue")
        self.spotify.volume(0, COMPUTER_ID)
        self.play()
        if way == 'hard':
            print("hard clearing")
            self.spotify.add_to_queue(DEECIEN_SONG)
            self._clear_queue_till(DEECIEN_SONG)
        else:
            self.spotify.add_to_queue(MEGAN_BITCH_SONG)
            self._clear_queue_till(MEGAN_BITCH_SONG)

        self.stop()
        print("queue cleared")
        self.spotify.volume(100, COMPUTER_ID)

    def _get_current_playing_song_id(self):
        return self.spotify.current_playback()['item']['id']
