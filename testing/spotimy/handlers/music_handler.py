import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

from testing.spotimy.handlers.playlist_handler import PlaylistHandler
from testing.spotimy.handlers.song_handler import SongHandler


class MusicHandler(PlaylistHandler, SongHandler):

    def __init__(self):
        self.sp_obj = self.authorize_token()
        PlaylistHandler.__init__(self, self.sp_obj)
        SongHandler.__init__(self, self.sp_obj)

    def authorize_token(self) -> sp.Spotify:
        oauth_obj = SpotifyOAuth(client_id='de2d9cc5b55945dbace895db7dbfec84',
                                 client_secret='d3ea340a2fd1471f819f91b14b1097f6',
                                 redirect_uri='http://localhost:8001/redirect',
                                 scope=['playlist-modify-private', 'user-follow-read', 'user-top-read','user-read-playback-position', 'playlist-read-collaborative','user-follow-modify', 'user-read-currently-playing', 'user-library-read','user-read-private', 'playlist-modify-public', 'user-read-email','user-read-recently-played', 'playlist-read-private', 'ugc-image-upload','user-read-playback-state', 'user-library-modify','user-modify-playback-state'])
        token = oauth_obj.get_access_token()['access_token']
        return sp.Spotify(token, client_credentials_manager=SpotifyClientCredentials(sleep_after_request=1))

    def start_playback(self, device_id: str):
        self.sp_obj.start_playback(device_id)

    def stop_playback(self, device_id: str):
        self.sp_obj.pause_playback(device_id)

