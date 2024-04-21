import os
import time

IPODDIR = "/dev/sdb2"

to_mount ="/home/becker/ipodmnt"
fusemount = "/home/becker/nwmnt"

os.system(f"sudo mount {IPODDIR} {to_mount}")
print("mounted first")

#time.sleep(2)

#os.system(f'IPOD_DIR="{to_mount}" fusepod {fusemount}')
#print("mounted second")

#time.sleep(2)


