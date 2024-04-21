import requests
import json
#from spotdl import Spotdl
from spotipod.secret import client_id, client_secret
from ipod_ctrl.control import IpodController

import time
from spotipod.spotify_api import Spotify

album = "https://open.spotify.com/album/2g6eUnuvDUSkGdUDmc2vBy?si=u5uaq8N3R1u6V-c8rEDXQA"


access_token = ""

tracks = [
    #"https://open.spotify.com/intl-de/album/5D7GOcUkCiSEyvvWOLuPFj?si=NW2OxG_kSQ-oQvY1VEfVbg",
    #"https://open.spotify.com/intl-de/album/0YUnrGKMe9iS6d26I24YFG?si=irJsbCT9T4OhAui7ixdvk",
    #"https://open.spotify.com/intl-de/album/2jyO4fGKpRJSHh8KCrvrBD?si=bh19o5GmTx-dAhZQ1wv2KA",
    #"https://open.spotify.com/intl-de/album/6l917ziBG07nTM0CDjAxwb?si=hwKVrIF8QLOulPeDdHwKRw",
    #"https://open.spotify.com/intl-de/album/5LL1Nuf6MAGacLVGtXAT4h?si=fM1ZQcpoQlS6iCB4xQHQrw",
    #"https://open.spotify.com/intl-de/album/2OT5X05C3oszyvJJra6VxI?si=ZcMnjch3SE-2X3m4H7vMmQ",
    #"https://open.spotify.com/intl-de/album/0oK1glMIKcHmAsDzhnxNpO?si=XpZiyfgwQri0mIGbb4Ee0w",
    #"https://open.spotify.com/intl-de/album/5Smkfw2oCHkVJeGWgo0ylD?si=2nzAUz60QsiLIoTXj9gLew",
    #"https://open.spotify.com/intl-de/album/0GyLgE1cRLcOUfsnhRplXI?si=ZtAnv2aFSQ2IMZmIU3NSOg",
    #"https://open.spotify.com/intl-de/album/0GyLgE1cRLcOUfsnhRplXI?si=ZtAnv2aFSQ2IMZmIU3NSOg",
    #"https://open.spotify.com/intl-de/album/4AG9l8sVfZ4OhBRjuOFnze?si=oRjzdxZJQ3qY50jQkoxuqw",
    #"https://open.spotify.com/intl-de/album/1oMWwWSqcGxpn2YhsYkNt6?si=c3lcEoobTQ-Lr2mdwSNbkAv",
    #"https://open.spotify.com/intl-de/album/5dFqidhoMEed1Nx9gO9M71?si=NggDbUoQQLybtFb2e8PQtQ",
    #"https://open.spotify.com/intl-de/album/53IJ9Yh8EcaYpEw1tSarDn?si=f3jbW5O2SAKCQ3egmQYrtw",
    #"https://open.spotify.com/intl-de/album/03iNJiD9tUpIdBLvHYwZwT?si=-zn0MdCqRp2bX4-2EN5HUg",
    #"https://open.spotify.com/intl-de/album/7flMvR3hmHgwMpnTsdVApW?si=DAfIIaqkTDujgGpL1I3uWg",
    #"https://open.spotify.com/album/26QqnKS4AMOTmHsl2HfbnZ?si=o_DIzlTWTpWDjn6U7RrEEg",
    #"https://open.spotify.com/album/110qiwftp3IZuEj6Lp5LqB?si=eZac3mpwRz27VYAiscxnrw",
    #"https://open.spotify.com/album/1JR6UkErYirK1yiwTf1fwj?si=hVNZs9ROSxWAErGF7i7-VA",
    #"https://open.spotify.com/album/0SyO17NG4tEWWMc0lRocfb?si=Ml2Z2tHyQ8266ifYAWE-fg",
    #"https://open.spotify.com/album/5B76QDHjmGhG96FOdZmNBx?si=FikDq_XJT4WyY3aZ7ZmvBA",
    #"https://open.spotify.com/album/50MeziN5Do8zDtN4wINTTS?si=tWk6BkPgRY-ckxqoD4I1Xg",
    #"https://open.spotify.com/intl-de/album/0cTOvcvrbNiaiv4WXEUHzT?si=saOJZFgySbmQDlWI4vv-1w",
    #"https://open.spotify.com/intl-de/album/58IwNbkCL527REhNX7emWv?si=7Ve0v7rHSkSyTeazdRVcvA",
    #"https://open.spotify.com/intl-de/album/3yuCvOuQzeRrUJ4IUZJU65?si=LtDEZTUTS8qjue4mbmctbA",
    "https://open.spotify.com/album/672lt6au46TYlrsYLLvTTa?si=igO2R0QbTLCUnxKoDOHERw"
]

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
    for song in tracks:
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

def test_sync():
    from ipod_ctrl.sync import SyncController
    SyncController().sync()


def test_mnt():
    import os
    ls = os.listdir("/dev")

    #always starts with sd
    sds = [x for x in ls if "sd" in x]

    #get the letter afterwarfds
    sds = list(set([x[:3] for x in sds]))
    if len(sds) == 0:
        raise SystemError("Mount point not found")
    
    elif len(sds) > 1:
        raise SystemError("More than one mount point found.")
    
    print(sds[0] + "2")


#get_access_token()
#test_get()

#test_down()
#test_endpoint()

#test_spotdl()
#test_get_tracks()

def test_add():
    tracks_to_add = [
        "6cyvFvADtpjU64L1gQWTK0",
        "13haVESplLXnO0ktYj1Xuu"
    ]
    from spotipod import constant as c
    import os
    cwd = os.getcwd()
    paths = [f"{cwd}/{c.MUSIC_FOLDER}/{track}.mp3" for track in tracks_to_add]

    IpodController().add(paths)

test_add()