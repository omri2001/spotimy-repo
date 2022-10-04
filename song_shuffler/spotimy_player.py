from spotipy import Spotify

from playlist_manipulator.playlist import Playlist
from common.spotify_parsers import COMPUTER_ID


class SpotimyPlayer:

    def __init__(self, spotify_obj: Spotify):
        self.spotify = spotify_obj
        self.playlist = Playlist.init_empty()
        self.next_in_line = None
        self.stopped = False
        self.playing = False

    def play(self):
        assert not self.playlist.empty
        self.stopped = False
        self.playing = True

        if not self.next_in_line:
            song = self.playlist.play_song()
            self.spotify.add_to_queue(song.id, COMPUTER_ID)

        self.spotify.start_playback(COMPUTER_ID)

        while (not self.stopped) or (not self.playlist.empty):
            if not self.next_in_line:
                song = self.playlist.play_song()
                self.next_in_line = song
                self.spotify.add_to_queue(song.id, COMPUTER_ID)
            else:
                if self._get_current_playing_song_id() == self.next_in_line.id:
                    self.next_in_line = None

    def stop(self):
        self.spotify.pause_playback(COMPUTER_ID)
        self.stopped = True
        self.playing = False

    def _get_current_playing_song_id(self):
        return self.spotify.current_playback()['item']['id']
