# spotipod

Put your spotify music onto your old iPod!

Send spotify links from your phone to a server, let it handle the download and sync it to your iPod with only 1 Click.



The application consists of 3 components:

## 1. spotipod-mobile

Flutter app that lets you send links to spotipod server.<br>
Find it here:
https://github.com/paulbenediktbecker/spotipod_client

## 2. spotipod-server
Api that takes in links from different users and forwards them on demand to the worker. Basically just Flask + Kafka.

## 3. spotipod-worker
Worker that pulls data from spotipod-server, downloads it using 


# Usage

How i am using it:


We have 3 components that needs to be started 
```
docker-compose up -d
python main.py
python worker.py
```

# Libraries used
### spotDL for downloading
https://github.com/spotDL/spotify-downloader

### gnupod for syncing to iPod
https://www.gnu.org/software/gnupod/ <br>
The version there is quite outdated and does not work properly with current libraries.
You can see the version i got running here:
https://github.com/paulbenediktbecker/gnupod

# Other libraries worth mentioning
https://github.com/dstaley/sharepod-lib
https://github.com/dstaley/clickwheel

# Roadmap
- full dockerization
- different users possible on server, so that multiple spotipod-mobile clients can send to one server.
- two modes on server and worker: 
    1. Let worker run on same device as server and let it instantly download the files when it arrives (how i would like to use it)
    2. Let worker run on different device than server and let it pull the jobs on demand (e.g. a friend of mine sends links from her phone to my server and can download and songs on her own laptop)

# todo
worker muss die möglichkeit haben, an den server rückzumelden, dass:
- Die jsons der daten müssen persitiert werden
- outsource den sync zum worker. -> mach startsync file
- split requirements txt from server and worker
1. der job abgearbeitet wurde
2. Musik auf den ipod geladen wurd
3. Punkt 2 nochmal manuell nachzuholen