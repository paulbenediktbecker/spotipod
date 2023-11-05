import requests
import json
import datetime

from secret import client_id, client_secret

class Spotify(object):
    
    def __init__(self):
        self.access_token = None
        self.token_type = None
        self.time_last_authorized = None
        self.secs_token_valid = 0
        pass

    def authorize(self):
        ct = datetime.datetime.now()
        if not self.time_last_authorized:
            self.renew_auth_token()
            return 
        
        if ct > (self.time_last_authorized + self.secs_token_valid):
            self.renew_auth_token()


    def renew_auth_token(self):
        url = "https://accounts.spotify.com/api/token"
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
        resp = requests.post(headers =  header, url = url, data=body)
        content = json.loads(resp.content.decode())
        self.access_token = content["access_token"]
        self.token_type = content["token_type"]
        self.secs_token_valid = int(content["expires_in"])
    
    def get_tracks_of_album(self, album_id):
        header = {"Authorization": f"Bearer {self.access_token}"}
        url = "https://api.spotify.com/v1/albums/6tAlnBBhfQ2JKgccEXox4p/tracks"
        resp = requests.get(headers=header, url= url)
        content = json.loads(resp.content.decode())

        song_ids = [x["id"] for x in content["items"]]
        print(song_ids)