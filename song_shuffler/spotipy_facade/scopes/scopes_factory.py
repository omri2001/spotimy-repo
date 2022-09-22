from typing import List


class ScopeFactory:

    @classmethod
    def all_scopes(cls) -> List[str]:
        return ['playlist-modify-private', 'user-follow-read', 'user-top-read', 'user-read-playback-position',
                'playlist-read-collaborative', 'user-follow-modify', 'user-read-currently-playing',
                'user-library-read', 'user-read-private', 'playlist-modify-public', 'user-read-email',
                'user-read-recently-played', 'playlist-read-private', 'ugc-image-upload',
                'user-read-playback-state',
                'user-library-modify', 'user-modify-playback-state']
