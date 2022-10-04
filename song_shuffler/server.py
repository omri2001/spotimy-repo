import uvicorn
import spotipy as sp
from fastapi import FastAPI, requests
from pydantic import BaseModel

from client import Client

app = FastAPI()

class ClientInp(BaseModel):
    client_id: str
    client_secret: str



@app.api_route('/')
def login(client_inp: ClientInp):
    client = Client

@app.api_route('/play')
def resume_playback(client: Client):

@app.api_route('/{')
def main_app():
    token = list(requests.query_params.values())[0]
    print(token['access_token'])
    return 'init app'

if __name__ == '__main__':
    uvicorn.run("server:app", port=8001, log_level="info", reload=True)


def get_auth_for_login():
    user_id = 'de2d9cc5b55945dbace895db7dbfec84'
    user_secret = 'd3ea340a2fd1471f819f91b14b1097f6'
    redirect_url = 'http://127.0.0.1:8001/redirect'
    scopes = list(tk.scope.every)
    return sp.SpotifyOAuth(user_id, user_secret, redirect_url, scopes)

