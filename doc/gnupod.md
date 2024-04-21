# notes 
i added my ipod to non auto mount list. You have to make sure, your gui does not automatically mount it.
https://unix.stackexchange.com/questions/333721/how-to-stop-auto-mounting-of-devices-in-ubuntu


also, to make gnupod work i had to add 
```
#!/usr/bin/perl
```

as the first line in every .pl file in src
# installl make etc
```
sudo apt-get install build-essential
```
# installing gnupod
download https://www.blinkenlights.ch/gnupod-dist/stable/gnupod-0.99.tgz

GNUPOD Doc foudn here: https://www.gnu.org/software/gnupod/gnupod.html

### perl packages
```
install perl packages:
```
sudo apt-get install libfile-ncopy-perl
sudo apt-get install libmp3-info-perl
sudo apt-get install libunicode-string-perl
sudo apt-get install libxml-parser-perl
sudo apt-get install libxml-simple-perl
```


#install gnupod
cd to a new dir, in my case /git/gnupod
```

sudo make install

```

