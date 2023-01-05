from testing.spotipy_facade.music_handler.playlists_manager import PlaylistManager
from testing.spotipy_facade.music_handler.songs_manager import SongManager


class MusicManager(SongManager, PlaylistManager):

    def __init__(self, spotify_obj):
        SongManager.__init__(self, spotify_obj)
        PlaylistManager.__init__(self, spotify_obj)
