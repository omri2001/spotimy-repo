from testing.client import Client

playlist_id = '76d0HCZ3huyzSTZd112j5G'
MEGAN_BITCH_SONG = '06scTb0zbkxYNgpAB3J9fN'
NEVERITA_SONG = '31i56LZnwE6uSu3exoHjtB'
DEECIEN_SONG = '50jULvLQIKWfZWGIh3rYEd'

if __name__ == '__main__':
    client = Client()
    client.load_queue_from_playlist(playlist_id)
    print(client.get_queue())
    client.add_song_to_queue(NEVERITA_SONG)
    print(client.get_queue())
