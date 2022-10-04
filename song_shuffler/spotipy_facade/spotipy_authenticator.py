from typing import List

from spotipy import SpotifyOAuth


class SpotipyAuthenticator:

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scopes: List[str]):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scopes = scopes

    def get_token(self):
        oauth = SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri, scope=self.scopes)
        token = oauth.get_access_token()
        return token['access_token']





