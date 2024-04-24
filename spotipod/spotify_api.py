import requests
import json
import datetime
import os
from .secret import client_id, client_secret
from . import constant as c
class Spotify(object):
    
    def __init__(self):
        self.access_token = None
        self.token_type = None
        self.time_last_authorized = None
        self.secs_token_valid = 0

        self.ARTWORK_FOLDER = os.environ("ARTWORK_FOLDER")

        os.makedirs(self.ARTWORK_FOLDER,exist_ok=True)
        

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
        self.authorize()
        header = {"Authorization": f"Bearer {self.access_token}"}
        url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
        resp = requests.get(headers=header, url= url)
        content = json.loads(resp.content.decode())

        song_ids = [x["id"] for x in content["items"]]
        return song_ids
    
    def get_coverart(self,track_id):
        self.authorize()
        header = {"Authorization": f"Bearer {self.access_token}"}
        url = f"https://api.spotify.com/v1/tracks/{track_id}"
        resp = requests.get(headers=header, url= url)
        content = json.loads(resp.content.decode())
        print("hi")
        if "album" in content:
            if "images" in content["album"]:
                
                imgs = content['album']['images']
                if not imgs or len(imgs)< 1:
                    return False

                min= None
                min_index = None

                #finding smallest entry
                for index, img in enumerate(imgs):
                    if "height" not in img:
                        continue
                    if min_index is None:
                        min_index = index
                        min = img["height"]
                        continue
                    if img["height"] < min:
                        min = img["height"]
                        min_index = index

                img = imgs[min_index]
                img_url = img["url"]

                #download and save img
                img_data = requests.get(img_url).content
                with open(f'{self.ARTWORK_FOLDER}/{track_id}.jpg', 'wb') as handler:
                    handler.write(img_data)
                return True
                
        return False

        