import json
import os 

from spotify_api import Spotify
from secret import client_id, client_secret

from spotdl import Spotdl, DownloaderOptionalOptions



FILENAME = "data.json"

class Storage(object):

    def __init__(self):
        self.data = None
        self.init_file()
        self.spotify = Spotify()
        
        options = DownloaderOptionalOptions(output="music/{track-id}.{output-ext}")
        self.spotdl = Spotdl(client_id=client_id, client_secret=client_secret,downloader_settings=options)
        pass

    def init_file(self):
        if os.path.isfile(FILENAME):
            with open(FILENAME, 'r') as f:
                self.data = json.load(f)
            return
        

        with open(FILENAME, "w") as f:
            f.write("{}")
        self.data = {}

    def add_album(self, album_id):
        if album_id is None:
            return
        
        if "albums" not in self.data:
            self.data["albums"] = {}

        if album_id in self.data["albums"]:
            return
        
        tracks = self.spotify.get_tracks_of_album(album_id)
        self.data["albums"][album_id] = tracks

        for track in tracks:
            self.add_track(track)

    def add_track(self, track_id):
        if track_id is None:
            return
        
        if "tracks" not in self.data:
            self.data["tracks"] = []

        if track_id in self.data["tracks"]:
            return
        

        songs = self.spotdl.search(
            ['https://open.spotify.com/intl-de/track/6b6nLUteRmUBw6AVlwy8pQ?si=405a1e00d434415e'])

        song, path = self.spotdl.download(songs[0])
        self.data["tracks"].append(track_id)

    


    