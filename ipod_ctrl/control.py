import subprocess
import os

def run(string):
    subprocess.run(string)

def runs(ls):
    subprocess.run(ls, shell=True)

class IpodController(object):

    def __int__(self):
        self.mnt = ""
        self.base_dir = "/home/becker/git/gnupod/gnupod-0.99/src"

    def is_mounted(self):
        stat_info = os.statvfs(self.mnt)
        return stat_info.f_bfree != stat_info.f_blocks
    
    def ensure_mounted(self):
        if not self.is_mounted():
            self.mount()
    
    def mount(self):
        mnt_point = self.get_usb_point()
        run(f"sudo mount {mnt_point}")
        self.mnt =mnt_point

    def add(self, mp3_file):
        self.ensure_mounted()
        run(f"{self.base_dir}/gnupod_addsong.pl -m {self.mnt} {mp3_file}")

    def release(self):
        cmd = f"{self.base_dir}/mktunes.pl -m {self.mnt}"
        run(cmd)
        self.unmount()

    def unmount(self):
        run(f"sudo umount {self.mnt}")

    def get_usb_point(self):
        ls = os.listdir("/dev")

        if "sdb2" not in ls:
            raise SystemError("Mount point not found")
        
        return "/dev/sdb2"
    
