

class PlaylistHandler:

    def __init__(self, spotify, username):
        self.spotify = spotify
        self.username = username

    def get_playlist_songs(self, playlist):
        playlist_id = self.get_playlist_id(playlist)
        return [song.track for song in self.spotify.all_items(self.spotify.playlist_items(playlist_id))]

    def get_all_playlists(self):
        return [playlist for playlist in self.spotify.all_items(self.spotify.playlists(self.username))]

    def get_selfmade_playlists(self):
        return [playlist for playlist in self.get_all_playlists() if playlist.owner.id == self.username]

    def get_library_playlists(self):
        all_playlists = self.get_all_playlists()
        return [playlist_info for playlist_info in all_playlists if playlist_info.owner.id != self.username]

    def get_playlist_id(self, playlist):
        return playlist.id

    def get_playlist_name(self, playlist):
        return self.spotify.playlist(playlist.id).name

    def get_playlists_names(self, playlists):
        return [self.get_playlist_name(playlist) for playlist in playlists]

    def get_playlist_from_name(self, playlist_name):
        all_playlist = self.get_all_playlists()
        playlist = [playlist for playlist in all_playlist if self.get_playlist_name(playlist) == playlist_name]
        if len(playlist) >= 1:
            return playlist[0]
        else:
            print("wrong playlist name, playlist name not in list")