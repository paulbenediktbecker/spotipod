from spotdl import Spotdl, DownloaderOptionalOptions
import os

output_folder = "/Users/becker/git/spotipod/music"
options = DownloaderOptionalOptions(bitrate="128k", format="flac", ffmpeg_args="-ar 44100", skip_album_art=False)


client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

spotdl = Spotdl(client_id=client_id, client_secret=client_secret,downloader_settings=options)

ids=[
    #"https://open.spotify.com/album/1KjOBKZLm98fQ31PoWJBjT?si=OiTCnoDMReSsogxIeknwRg", #abrunzati kult
    #"https://open.spotify.com/album/1oMWwWSqcGxpn2YhsYkNt6?si=66GCI-yRS6-Bn6pP5KjGlg", #chuba glas
    #"https://open.spotify.com/album/6Tlq4ccVITktCuFUDr8ceE?si=s_Rg764uTsWu4tpBQjt3_A", #mele nicts macht sinn
    #"https://open.spotify.com/album/0HICsKReOoeoblyeiLClEd?si=xIAIzvovQSitPD7CY1dXgw", #dilla
    #"https://open.spotify.com/album/1NkctVTc6vjJ6j0U606B7g?si=xSxjzfBETcaDsREROxElIw", #kargo
    #"https://open.spotify.com/album/6tAlnBBhfQ2JKgccEXox4p?si=N_QbxZ1rRruXI7pPI-rOjw", #hinterland  
    #"https://open.spotify.com/album/418d2w3Snw5WkZCvKK7jw9?si=e2a9sdH1TxOGiarTPCyFsg", #yannick haverland 
    #"https://open.spotify.com/album/3tOztFpIobGXqNv2a8J0DV?si=BFID-czkR66dokkX7iYavw", #veri bulletholes
    #"https://open.spotify.com/album/4AG9l8sVfZ4OhBRjuOFnze?si=y1X59Kv8RxSYt2qG_NtI1w", #veri adhs
    #"https://open.spotify.com/album/4gL18Qzv6bMtLV2zYw7K9J?si=40voTxx_QQu-532TzH3IwQ", #esther happy worstday
    #"https://open.spotify.com/album/5D7GOcUkCiSEyvvWOLuPFj?si=PL5X3YaFRxCXQr8PxDz58w", #disarstar rfa
    #"https://open.spotify.com/album/3StYo4OicJlkTKLQFOgA4B?si=reLFnEv2Q4G-rjflgCLYtQ", #disarstar overdose
    #"https://open.spotify.com/album/6DEjYFkNZh67HP7R9PSZvv?si=_XCJiPDPSC65DLWyKuxD-w", #reputatoin
    #"https://open.spotify.com/album/1NAmidJlEaVgA3MpcPFYGq?si=FnJTs3gwRzWWb9zV9Th6bg", #lover
    #"https://open.spotify.com/album/64LU4c1nfjz1t4VnGhagcg?si=xeEGf8a0ReSIx_0DjyeH4Q", #1989
    #"https://open.spotify.com/album/78qD6T34x0zDcg3PFyh4zl?si=li2EIYZ-RgGuz3FbeSFtdQ", #POP
    #"https://open.spotify.com/album/72Tg8IM0FR3KOIxGTRElvU?si=DLX3QZaGSUOJ8Jw6gqMQdw", #NIE
    #"https://open.spotify.com/album/0NFLRCJFx8z2DL7eqGql4D?si=KZYXJmaBQLSrZ2aTGEMjUg", #TOD
    #"https://open.spotify.com/album/6Ud07gmj5Nfm2ip6bhL5Rl?si=y5HBY09pRNGck-BbM-jGNA", #hamburger aufstand
    #"https://open.spotify.com/album/6yWb7ry1iFU4jCR45L6gCd?si=qGK4KR3UR-uWNUoDb_7j-w", #majan skits
    #"https://open.spotify.com/album/5aZ8DrzC2oyQzpJ5Uipufq?si=jm0Pm314SHSdaMroNamYEQ", #majan oh
    #"https://open.spotify.com/album/48xBOWLlBupgfhNKkErgDJ?si=at_5ye_sSwuwjlURkazu9A", #majan boi
    #"https://open.spotify.com/album/5dFqidhoMEed1Nx9gO9M71?si=CqTJ9DTJR4Kt78M97ai34A", #nie verliebt
    #"https://open.spotify.com/album/7pEVxmXGwVioPkQtRI1frc?si=IZMDQAG8RKGs1AYkisF4ig", #kleine feuer
    #"https://open.spotify.com/album/6Q5jcgLicbskXiZCBHS07A?si=h1J3rmqlSQCc5v8GuHt3RA", #kalte liebe sucht und drang
    #"https://open.spotify.com/album/4fiPokWbjnuxVCIKVl7bCG?si=d9iIwb7fSAePlyZA5eH2sg", #kalte liebe schall und schweiß
    #"https://open.spotify.com/album/2Q1EjwzkRPhT1WKPLitYxH?si=BxSCWRPgSSmlYME5qNpx4w", #keine nacht für niemand
    #"https://open.spotify.com/album/7bPaSU0uQ9zT2Dez8Ogch2?si=rGTJr_OKRROQ62B-JRca4A", # in schwarz 
    #"https://open.spotify.com/album/3f48kV1gGqmwGYae1bYgU9?si=BKHfTj7BSKGK42l1zGlhQA", #mit k
    #"https://open.spotify.com/album/022DrG7Wp2PSCwzuD0bSzT?si=btVx_vkaTlGmu0AuX3L8-Q", # fall out boy american beauty / psycho
    #"https://open.spotify.com/album/5WuZ1IE5sEBIRSlJUcXjdq?si=QpCev79LQFeO15eO_u3ewA", #zartmann schönhauser
    #"https://open.spotify.com/album/6cEVfMd0XVocPbRrYkVY5H?si=YBFe3sNoQfqRspYamovPyA", #stadtaffe
    #"https://open.spotify.com/album/4Z4FErymthnN4ctJdKRgko?si=zfjBlrvUQj67HEivSQh0Dw", #Billy Talent
    #"https://open.spotify.com/album/0cTOvcvrbNiaiv4WXEUHzT?si=9Shv94_ITR2nKJN3m6n4Kg", #Billy Talent II
    #"https://open.spotify.com/album/58IwNbkCL527REhNX7emWv?si=dr2Rf4ljT8KmMQHp5_ayWw", #Billy Talent III
    #"https://open.spotify.com/album/5LL1Nuf6MAGacLVGtXAT4h?si=KdfTPlKTSvioz2ks9OB-SA", #Lost Tape
    #"https://open.spotify.com/album/2OT5X05C3oszyvJJra6VxI?si=T_t8qBZ7Sze5JJCJZbuU6A", #Phase
    
    
    #"https://open.spotify.com/album/4VDX4YuDzvaRPfHaZ4FrFV?si=o_xI6L7pSn233tKLofRGRw", #title flight floral green
    #"https://open.spotify.com/album/4KX91DYlU4n9uqHdN9hC6J?si=CbYtt7sNSzyuaUsYZSIiEw", #ben hovard every kingdom
    #"https://open.spotify.com/track/6FgAH2lOrWWcFhXRDjhKrT?si=77e9a38cc0264cac", #war das schon alles
    "https://open.spotify.com/album/4GGazqHvuKwxBjWLFaJkDL?si=_3InDoUoRXKI8cJXUEzacQ", #justice, justice
    "https://open.spotify.com/album/5Dbax7G8SWrP9xyzkOvy2F?si=1LAY3T3vSZCi71rqW7jy2Q", #the wall, pink floyd
    "https://open.spotify.com/album/6uSnHSIBGKUiW1uKQLYZ7w?si=fxmpHTGtQtOQkpRuh3_K_w", #from the fires, greta van fleet
    "https://open.spotify.com/album/2tlTBLz2w52rpGCLBGyGw6?si=HixebGEASUKZzOsUvZGz5Q", #minutes to midnight, linkin park
    "https://open.spotify.com/album/1QGXwt2LukvLgFomHlhC41?si=430YOeeVTTWPTLhFAcbIjQ", #rocket science, mael jonas
    "https://open.spotify.com/album/6ApYSpXF8GxZAgBTHDzYge?si=rB2hLgMPQ6-4gtQc8h7tjA", #pray for the wicked, panic at the disco
]
#songs = spotdl.search(ids)

#results = spotdl.download_songs(songs)

from worker.spotify_api import Spotify
spot = Spotify(client_id, client_secret)
for id in ids:
    x = id.split("/")[-1].split("?")[0]

    songs = spot.get_tracks_of_album(x)
    for song in songs:
        spot.get_coverart(song)