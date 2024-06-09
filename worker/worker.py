import requests
import os
import time

from spotdl import Spotdl, DownloaderOptionalOptions
from kafka import KafkaConsumer, KafkaProducer

from worker.spotify_api import Spotify

class Worker(object):

    def __init__(self):
        options = DownloaderOptionalOptions(output="music/{track-id}.{output-ext}")

        client_id = os.environ.get("SPOTIFY_CLIENT_ID")
        client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
        self.spotdl = Spotdl(client_id=client_id, client_secret=client_secret,downloader_settings=options)
        self.spotify = Spotify(client_id=client_id, client_secret=client_secret)

        self.base_url = os.environ.get("BASE_URL")
        self.port = os.environ.get("PORT")
        self.secret_key = os.environ.get("SECRET_KEY")

    def download_song(self, id):

        print(f"ID arrived at Spotdl: {id}", flush=True)
       
        songs = self.spotdl.search(
            [f'https://open.spotify.com/intl-de/track/{id}'])

        results = self.spotdl.download_songs(songs)
        #song, path = self.spotdl.download(songs[0])

    def download_artwork(self,id):
        try:
            self.spotify.get_coverart(id)
        except Exception as e:
            pass

    def sync_ipod(self):
        pass


    def work(self):
        secs_to_sleep = 2

        headers = {
            "Authorization": f"Bearer {self.secret_key}"
        }
        url= f"{self.base_url}:{self.port}/job"
        while True:
            
            try:
               
                response = requests.get(
                    url=url,
                    headers=headers,
                    timeout=1
                )
                print("Request done.")
                if response.status_code == 200: #if success
                    print("received 200")

                    data = response.json()
                    val = data["val"]
                    key = data["key"]

                    if key == "download_track":
                        print(f"received id {val} for track download")
                        self.download_song(val)

                    elif key == "download_artwork":
                        print(f"received id {val} for artwork download")
                        self.download_artwork(val)
                    elif key == "sync":
                        self.sync_ipod()

                    #ToDo accept job
                    continue #skip sleep
                

                if response.status_code == 404: #no new job
                    print("No new job.")
                else:
                    print(f"Error at fetch job: {response.status_code}")

                time.sleep(secs_to_sleep)
                
                
            except Exception as e:
                time.sleep(secs_to_sleep)
