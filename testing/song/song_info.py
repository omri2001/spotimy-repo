from dataclasses import dataclass

@dataclass
class SongInfo:
    name: str = None
    id: str = None
    duration: int = None
    tempo: float = None
    energy: float = None
    valence: float = None
    liveness: float = None
    danceability: float = None
    popularity: float = None
    instrumentalness: float = None
    acousticness: float = None
    speechiness: float = None
