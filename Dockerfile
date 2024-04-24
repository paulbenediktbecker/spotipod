FROM python:3.9

WORKDIR /usr/app


######################################## ENV

ENV MUSIC_FOLDER=music
ENV ARTWORK_FOLDER=$MUSIC_FOLDER/artwork
ENV MUSIC_DB_FILE=./data.json
ENV MUSIC_ON_IPOD_FILE=./on_ipod.json
ENV MNT_DIR="/mnt/ipod"

######################################## files

COPY spotipod ./spotipod
COPY ipod_ctrl ./ipod_ctrl
COPY api.py .
COPY worker.py .
COPY requirements.txt .
COPY EMPTY_data.json $MUSIC_DB_FILE
COPY EMPTY_on_ipod.json $MUSIC_ON_IPOD_FILE


######################################## Requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt install -y ffmpeg
RUN apt-get install -y libfile-ncopy-perl
RUN apt-get install -y libmp3-info-perl
RUN apt-get install -y libunicode-string-perl
RUN apt-get install -y libxml-parser-perl
RUN apt-get install -y libxml-simple-perl
RUN perl -MCPAN -e "install Digest::SHA1"
RUN apt install -y imagemagick

################## GNUPOD 

RUN mkdir gnupod
RUN git clone https://github.com/paulbenediktbecker/gnupod.git
WORKDIR /usr/app/gnupod
RUN autoreconf --install 
RUN ./configure
RUN make install
WORKDIR /usr/app


#############################
ENV PYTHONPATH /usr/app
CMD ["python", "api.py"]


# build command
# docker compose build