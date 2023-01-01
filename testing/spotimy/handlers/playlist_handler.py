import time
from typing import List

import spotipy as sp
from tqdm import tqdm

from testing.song.Song import Song
from testing.spotimy.handlers.song_handler import SongHandler


class PlaylistHandler:

    def __init__(self, sp_obj: sp.Spotify):
        self.sp_obj = sp_obj
        self.song_handler = SongHandler(self.sp_obj)

    def get_playlist_songs_from_id(self, playlist_id: str) -> List[Song]:
        songs = []
        for spotipy_track in tqdm(self.sp_obj.playlist(playlist_id)['tracks']['items']):
            song_id = spotipy_track['track']['id']
            songs.append(self.song_handler.get_song_by_id(song_id))
            time.sleep(1.5)
        return songs
