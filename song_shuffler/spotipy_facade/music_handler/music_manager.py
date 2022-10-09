from song_shuffler.spotipy_facade.music_handler.albums import AlbumManager
from song_shuffler.spotipy_facade.music_handler.playlists_manager import PlaylistManager
from song_shuffler.spotipy_facade.music_handler.songs_manager import SongManager


class MusicManager(SongManager, PlaylistManager, AlbumManager):

    def __init__(self, spotify_obj):
        SongManager.__init__(self, spotify_obj)
        PlaylistManager.__init__(self, spotify_obj)
        AlbumManager.__init__(self, spotify_obj)

        # self.song_manager = SongManager(spotify_obj)
        # self.playlist_manager = PlaylistManager(spotify_obj)
        # self.album_manager = AlbumManager(spotify_obj)
