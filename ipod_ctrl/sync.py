from spotipod import constant as c
from .control import IpodController

import json 
import os

class SyncController(object):

    def __init__(self):
        self.ipod = IpodController()

    def sync(self):
        tracks_to_add = self.get_tracks_to_add()

     
        for track in tracks_to_add:
            path = f"{c.MUSIC_FOLDER}/{track}.mp3"
            artwork = self.get_artwork(track)

            self.ipod.add(path,artwork)
        self.ipod.release()

    def read_json(self, json_file):
        with open(json_file, "r") as f:
            data = json.load(f)
        return data
        
    def get_tracks_to_add(self):

        tracks_on_ipod = set(self.read_json(c.MUSIC_ON_IPOD_FILE)["tracks"])
        tracks_in_db = set(self.read_json(c.MUSIC_DB_FILE)["tracks"])

        tracks_to_add = list(tracks_in_db - tracks_on_ipod)
        return tracks_to_add

    def get_artwork(self, id):
        path = f"{c.ARTWORK_FOLDER}/{id}.jpg"
        if os.path.isfile(path):
            return path
        return None



    