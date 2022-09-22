

class AlbumHandler:

    def __init__(self, spotify):
        self.spotify = spotify

    def get_library_albums(self):
        return [album.album for album in self.spotify.all_items(self.spotify.saved_albums())]

    @property
    def get_id(self, album):
        return album.id

    def get_album_songs(self, album):
        album_id = self.get_id(album)
        return [song for song in self.spotify.all_items(self.spotify.album_tracks(album_id))]

    def get_album_name(self, album_id):
        return self.spotify.album(album_id).name

    def get_album_id_from_name(self, album_name):
        all_albums = self.get_library_albums()
        for album in all_albums:
            if album.name == album_name:
                return album.id





