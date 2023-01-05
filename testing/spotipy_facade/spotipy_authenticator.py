from spotipy import SpotifyOAuth


class SpotipyAuthenticator:

    def __init__(self):
        self.client_id = 'de2d9cc5b55945dbace895db7dbfec84'
        self.client_secret = 'd3ea340a2fd1471f819f91b14b1097f6'
        self.redirect_uri = 'http://localhost:8001/redirect'
        self.scopes = ['playlist-modify-private', 'user-follow-read', 'user-top-read', 'user-read-playback-position', 'playlist-read-collaborative', 'user-follow-modify', 'user-read-currently-playing', 'user-library-read', 'user-read-private', 'playlist-modify-public', 'user-read-email', 'user-read-recently-played', 'playlist-read-private', 'ugc-image-upload', 'user-read-playback-state', 'user-library-modify', 'user-modify-playback-state']

    def get_token(self):
        oauth = SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri,
                             scope=self.scopes)
        token = oauth.get_access_token()
        return token['access_token']
