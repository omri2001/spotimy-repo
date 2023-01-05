from typing import List

from spotipy import Spotify
from tqdm import tqdm

from testing.song.Song import Song
from testing.spotipy_facade.music_handler.songs_manager import SongManager
from testing.spotipy_facade.utils import get_all_pages


class PlaylistManager:

    def __init__(self, spotify_obj: Spotify):
        self.spotify = spotify_obj
        self.song_manager = SongManager(self.spotify)

    def get_playlist_songs(self, playlist_id: str) -> List[Song]:
        playlist_songs = []

        playlist_pager = self.spotify.playlist_items(playlist_id)
        for playlist_song in tqdm(get_all_pages(self.spotify, playlist_pager)):
            song_details = playlist_song['track']
            song = self.song_manager.get_song(song_details['id'], song_details)
            if song:
                playlist_songs.append(song)
        return playlist_songs