import os

IPODDIR = "/dev/sdb2"

to_mount ="/home/becker/ipodmnt"
fusemount = "/home/becker/nwmnt"

os.system(f"sudo fusermount -u {fusemount}")
print("added music")

os.system(f"sudo umount {to_mount}")

