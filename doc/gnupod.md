# notes 
i added my ipod to non auto mount list. You have to make sure, your gui does not automatically mount it.
https://unix.stackexchange.com/questions/333721/how-to-stop-auto-mounting-of-devices-in-ubuntu


also, to make gnupod work i had to add 
```
#!/usr/bin/perl
```

as the first line in every .pl file in src
you can use the add_shebang.py for that.

# installl make etc
```
sudo apt-get install build-essential
```


GNUPOD Doc foudn here: https://www.gnu.org/software/gnupod/gnupod.html

### perl packages

install perl packages:
```
sudo apt-get install libfile-ncopy-perl
sudo apt-get install libmp3-info-perl
sudo apt-get install libunicode-string-perl
sudo apt-get install libxml-parser-perl
sudo apt-get install libxml-simple-perl
sudo perl -MCPAN -e "install Digest::SHA1"
sudo apt install imagemagick

```


# installing gnupod
```
git clone https://git.savannah.gnu.org/git/gnupod.git
autoreconf --install 
./configure
make install
```

Replace FileMagic.pm and XMLhelper.pm at /etc/perl/GNUpod with the respecting files in this dir - the original ones are not compatible with todays perl. Works with Perl 5.34.0


