import subprocess
import os

from spotipod import constant as c

def run(string):
    print(string)
    p = subprocess.run(string)
  


def runs(ls):
    subprocess.run(ls, shell=True)

class IpodController(object):

    def __init__(self):
        self.mnt_dir = c.MNT_DIR
        self.sys_mnt = self.get_usb_point()
        self.base_dir = "/home/becker/git/gnupod/src"
        self.mount()

    def is_mounted(self):
        stat_info = os.statvfs(self.mnt_dir)
        return stat_info.f_bfree != stat_info.f_blocks
    
    def ensure_mounted(self):
        if not self.is_mounted():
            self.mount()
    
    def mount(self):

        #first unmount it, in case its mounted somewhere else
        self.unmount()

        run(["sudo" ,"mount", self.sys_mnt, self.mnt_dir])

    def add(self, mp3_file, jpg_file): 
        self.ensure_mounted()

        if jpg_file:
            cmd = ["sudo", "perl", f"{self.base_dir}/gnupod_addsong.pl" ,"-m", self.mnt_dir,"--artwork", jpg_file, mp3_file]

        else:
            cmd = cmd = ["sudo", "perl", f"{self.base_dir}/gnupod_addsong.pl" ,"-m", self.mnt_dir, mp3_file]
        run(cmd)


    def release(self):
        cmd = ["sudo", "perl",f"{self.base_dir}/mktunes.pl" ,"-m" ,self.mnt_dir]
        run(cmd)
        self.unmount()

    def unmount(self):
        run(["sudo","umount", self.sys_mnt])

    def get_usb_point(self):
        return "/dev/sdb2"
        ls = os.listdir("/dev")

        #always starts with sd
        sds = [x for x in ls if "sd" in x]

        #get the letter afterwarfds
        sds = list(set([x[:3] for x in sds]))
        if len(sds) == 0:
            raise SystemError("Mount point not found")
        
        elif len(sds) > 1:
            raise SystemError("More than one mount point found.")
        
        return "/dev/" + sds[0] + "2"
    
