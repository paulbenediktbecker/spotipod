import json
import os 
import threading
import time

#import asyncio
#asyncio.set_event_loop(asyncio.new_event_loop())

from worker import spotify_api

from flask import jsonify
from spotdl import Spotdl, DownloaderOptionalOptions
from kafka import KafkaConsumer, KafkaProducer

FILENAME = os.environ.get("MUSIC_DB_FILE")



class Storage(object):

    def __init__(self):
        self.data = None
        self.init_file()

        client_id = os.environ.get("SPOTIFY_CLIENT_ID")
        client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
        self.spotify = spotify_api.Spotify(client_id=client_id, client_secret=client_secret)

        #kafka producer  
        #kafka consumer
        self.consumer = KafkaConsumer(
            "my_favorite_topic", 
            bootstrap_servers='localhost:29092',
            auto_offset_reset='earliest', 
            group_id='your_consumer_group',
            max_poll_records=1,#only one per poll
            enable_auto_commit=False,#has to be manually commited

            
        )
        self.consumer.subscribe("my_favorite_topic")  
        
        
        #start downloader
        #worker = Worker()
        #thread = threading.Thread(target=worker.work)
        #thread.start()


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
        
        self.send_job_to_kafka(track_id)
        self.data["tracks"].append(track_id)
        self.persist()

    def persist(self):
        with open(FILENAME, 'w') as fp:
            json.dump(self.data, fp)

    def send_job_to_kafka(self, track_id):
            try:
                self.producer = KafkaProducer(bootstrap_servers='localhost:29092')
                # Produce a message to the specified topic
                self.producer.send("my_favorite_topic", key=b'download_track', value=track_id.encode())
                self.producer.send("my_favorite_topic", key=b'download_artwork', value=track_id.encode())
                self.producer.flush()  # Wait for any outstanding messages to be delivered
                print('Message sent successfully.')
            except Exception as e:
                print(f'Error producing message: {str(e)}')
            finally:
                self.producer.close()
            print(f"sent id {track_id}")

    def get_job(self):
        
        try:
            
            msg = self.consumer.poll(timeout_ms=20)

            if msg is None or msg == {}:
                print("should return 404")
                return {},404 # no job found
            
            print(msg)
            
            val = list(msg.values())[0][0].value.decode()
            key = list(msg.values())[0][0].key.decode()

            data = {
                "key": key,
                "val": val,
                "msg":msg,
            }

            return jsonify(data),200
        
        except Exception as e:
            print(f'Error consuming message: {str(e)}')
            return {},500
    
    def commit_job(self,msg):
        try:
            self.consumer.commit()
        except Exception as e:
            print(f'Error consuming message: {str(e)}')
            return {},500
    
    def update_ipod_file(self):
        with open(os.environ.get("MUSIC_ON_IPOD_FILE"), 'w') as fp:
            json.dump(self.data, fp) 


    
    