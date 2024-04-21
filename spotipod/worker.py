
from spotdl import Spotdl, DownloaderOptionalOptions
from kafka import KafkaConsumer, KafkaProducer

from secret import client_id, client_secret

from spotdl import Spotdl, DownloaderOptionalOptions
from kafka import KafkaConsumer, KafkaProducer


class Worker(object):

    def __init__(self):
        options = DownloaderOptionalOptions(output="music/{track-id}.{output-ext}")
        self.spotdl = Spotdl(client_id=client_id, client_secret=client_secret,downloader_settings=options)

        #kafka consumer
        self.consumer = KafkaConsumer("my_favorite_topic", bootstrap_servers='localhost:29092',
                                    auto_offset_reset='earliest', group_id='your_consumer_group')

    def download_song(self, id):

        print(f"ID arrived at Spotdl: {id}", flush=True)
       
        songs = self.spotdl.search(
            [f'https://open.spotify.com/intl-de/track/{id}'])

        results = self.spotdl.download_songs(songs)
        #song, path = self.spotdl.download(songs[0])

    def sync_ipod(self):
        pass


    def work(self):
        print("consuming")    
        try:
            # Poll for new messages
            for msg in self.consumer:
                val = msg.value.decode()
                key = msg.key.decode()

                if key == "download":
                    print(f"received id {val}")
                    self.download_song(val)

                elif key == "sync":
                    self.sync_ipod()
        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()

worker = Worker()
worker.work()