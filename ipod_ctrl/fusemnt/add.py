import os

fusemount = "/home/becker/nwmnt"

os.system(f". {fusemount}/add_files.sh /home/becker/6sSiz9JquC9CZVg1g7QVAQ.mp3")
print("added music")


os.system(f". {fusemount}/sync_ipod.sh [ -watch ]")
