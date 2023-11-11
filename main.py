import os
import subprocess

from flask import Flask, request

from storage import Storage


app = Flask(__name__)

storage = Storage()


@app.route('/add', methods=['GET'])
def add():
    link = request.args.get('link')
    
    if link is None:
        return "400"

    if "https://open.spotify.com" not in link:
        return "400"
    
    if "album" in link:
        album_id = link.split("album")[1][1:]
        if "?" in album_id:
            album_id = album_id.split("?")[0]

        storage.add_album(album_id)
        return "200"
    
    if "track" in link:
        track_id = link.split("track")[1][1:]
        if "?" in track_id:
            track_id = track_id.split("?")[0]

        storage.add_track(track_id)
        return "200"
    
    return "400" 
    


if __name__ == '__main__':
    app.run(debug=True)

    
