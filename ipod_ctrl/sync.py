from spotipod import constant as c
from .control import IpodController

import json 


class SyncController(object):

    def __init__(self):
        self.ipod = IpodController()

    def sync(self):
        tracks_to_add = self.get_tracks_to_add()

        paths = [f"{c.MUSIC_FOLDER}/{track}.mp3" for track in tracks_to_add]
       
        self.ipod.add(paths)

    def read_json(self, json_file):
        with open(json_file, "r") as f:
            data = json.load(f)
        return data
        
    def get_tracks_to_add(self):

        tracks_on_ipod = set(self.read_json(c.MUSIC_ON_IPOD_FILE)["tracks"])
        tracks_in_db = set(self.read_json(c.MUSIC_DB_FILE)["tracks"])

        tracks_to_add = list(tracks_in_db - tracks_on_ipod)
        return tracks_to_add

        




    