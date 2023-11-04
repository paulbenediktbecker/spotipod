import os
import subprocess

albums = [
    #"https://open.spotify.com/album/2r2r78NE05YjyHyVbVgqFn?si=oVyjkhemRGyj3IcHspJC5w",
    #"https://open.spotify.com/album/1RFWXLqxR7tP7hyunSO13H?si=71e842ce434b4f0f",
    #"https://open.spotify.com/album/4E7HxVevq5O1XmvWhCEKXS?si=6c778300f1324778",
    #"https://open.spotify.com/album/48xBOWLlBupgfhNKkErgDJ?si=Hxg6IWCtQSuhpBzIB98Sng",
    #"https://open.spotify.com/album/3f48kV1gGqmwGYae1bYgU9?si=DiW8yKe2T0encm-HrZ-xyw",
    #"https://open.spotify.com/album/4Om5A3TGYl8auFZRz0l2Sf?si=GUNOXmIJSSK4Ab4S0yyAWw",
    #"https://open.spotify.com/album/2Q1EjwzkRPhT1WKPLitYxH?si=2ykXfFJJR-eMHLSbtrsJlA",
    #"https://open.spotify.com/album/30t7VjbwgOEPY1ATeIL44h?si=ZYenPvOKQDOniQaxHRnU8Q",
    "https://open.spotify.com/album/1NkctVTc6vjJ6j0U606B7g?si=XOhBNbWXQaq_lQnGu6I-Mw",
    "https://open.spotify.com/album/6tAlnBBhfQ2JKgccEXox4p?si=k-4tJ3t9QOGlRb1rM6tdSQ",
    "https://open.spotify.com/album/2g6eUnuvDUSkGdUDmc2vBy?si=4Yv_jmE9RsyRNR8vzessoA",
]   


for alb in albums:
    cmd = "spotdl download " + alb
    os.system(cmd)
    
