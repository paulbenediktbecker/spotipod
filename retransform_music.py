import json
import os
# Open the JSON file and load its content
with open("data.json", "r") as file:
    data = json.load(file)  # Parse JSON into a Python dictionary


albums = data["albums"]

dir = "/media/music2"

for x in albums: 
    albdir = f"{dir}/{x}"
    if not os.path.exists(albdir):
        os.mkdir(albdir)

    songs = albums[x]

    songs = [f"{x}.mp3" for x in songs]

    #move file

    for song in songs:
        source = f"{dir}/{song}"
        if os.path.exists(source):
            target = f"{albdir}/{song}"
            os.rename(
                src=source,
                dst=target

            )

    