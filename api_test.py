import requests
import json
from spotdl import Spotdl
from secret import client_id, client_secret

import time
from spotify_api import Spotify

album = "https://open.spotify.com/album/2g6eUnuvDUSkGdUDmc2vBy?si=u5uaq8N3R1u6V-c8rEDXQA"


access_token = "BQCa_mn-zoIYjpBWXVOg82-3AQ4pt61uwIX-1OqZBn4vjXBJqf4Kar9j9MqqOONw5LHi50ghNOSoJyaADj2xcnqPxQaXSSapKMxBHQZKUY9bheICH9w"


def test_get():
    header = {"Authorization": f"Bearer {access_token}"}
    url = "https://api.spotify.com/v1/albums/6tAlnBBhfQ2JKgccEXox4p/tracks"
    resp = requests.get(headers=header, url= url)
    content = json.loads(resp.content.decode())

    song_ids = [x["id"] for x in content["items"]]
    print(song_ids)

def get_access_token():

    url = "https://accounts.spotify.com/api/token"
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    body = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
    resp = requests.post(headers =  header, url = url, data=body)
    print(resp)
    print("hi")
    content = json.loads(resp.content.decode())
    access_token = content["access_token"]
    token_type = content["token_type"]
    print(access_token)
    print(token_type)

def test_down():
        from spotdl import DownloaderOptionalOptions
        
        options = DownloaderOptionalOptions(output="music/{track-id}.{output-ext}")
        spotdl = Spotdl(client_id=client_id, client_secret=client_secret,downloader_settings=options)

        songs = spotdl.search(
            ['https://open.spotify.com/intl-de/track/6b6nLUteRmUBw6AVlwy8pQ?si=405a1e00d434415e'])

        #results = spotdl.download_songs(songs)
        song, path = spotdl.download(songs[0])

def test_endpoint():
    song = "https://open.spotify.com/intl-de/album/1f5h6JX9E8RO5zRW9ALMIf?si=Jlfs0yyjRqShUDY1A0nMkA"
    url = f"http://127.0.0.1:5000/add?link={song}"
    resp = requests.get(url)
    print(resp)

    input("press enter to continue")
    time.sleep(5)
    song = "https://open.spotify.com/intl-de/track/0jLSeolrFXlzTQQjAOAWli?si=faebd71ed82b48b0"
    url = f"http://127.0.0.1:5000/add?link={song}"
    resp = requests.get(url)
    print(resp)

def test_spotdl():
    from spotdl import Spotdl, DownloaderOptionalOptions
    options = DownloaderOptionalOptions(output="music/{track-id}.{output-ext}")
    spotdl = Spotdl(client_id=client_id, client_secret=client_secret,downloader_settings=options)

    ids = ["2R2lamRI2IqH1hA1pK8gUF", "0jLSeolrFXlzTQQjAOAWli"]
    for id in ids:
        songs = spotdl.search(
            [f'https://open.spotify.com/intl-de/track/{id}'])

        results = spotdl.download_songs(songs)
        song, path = spotdl.download(songs[0])

def test_get_tracks():
    spotify = Spotify()


    id = "1f5h6JX9E8RO5zRW9ALMIf"

    tracks = spotify.get_tracks_of_album(id)
    print("hi")



#get_access_token()
#test_get()

#test_down()
test_endpoint()

#test_spotdl()
#test_get_tracks()
