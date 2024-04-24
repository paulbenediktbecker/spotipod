import os
import subprocess
from functools import wraps

from flask import Flask, request

from spotipod.storage import Storage
from ipod_ctrl.sync import SyncController
from ipod_ctrl.control import IpodController


app = Flask(__name__)
SECRET_KEY = os.environ.get('SECRET_KEY')


storage = Storage()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            print(request.headers["Authorization"])
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Authentication Token is missing!",

                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            
            if token != SECRET_KEY:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        except Exception as e:
            return {
                "message": "Internal Server error.",
                "data": None,
                "error": str(e)
            }, 500

        return f(*args, **kwargs)

    return decorated

@app.route('/add', methods=['GET'])
@token_required
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
    

@app.route('/sync', methods=['GET'])
@token_required    
def sync():
    SyncController().sync()
    print("synced.")
    return "200"

@app.route('/test', methods=['GET'])
@token_required
def test():
    print("arrived")
    return "200"                                
    
def run():
    app.run(debug=True,host='0.0.0.0')

run()


                              
