from spotipy_facade.music_handler.albums import AlbumManager
from spotipy_facade.music_handler.playlists import PlaylistManager
from spotipy_facade.music_handler.songs import SongManager


class MusicManager(SongManager, PlaylistManager, AlbumManager):

    def __init__(self, spotify_obj):
        super().__init__(spotify_obj)
        # self.song_manager = SongManager(spotify_obj)
        # self.playlist_manager = PlaylistManager(spotify_obj)
        # self.album_manager = AlbumManager(spotify_obj)





