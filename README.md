# Tag-mp3
### Overview

This is a simple script which adds title and artist metadata tags to mp3 files based on the 
file names. For example, after running the script on a file with the name "Passenger - Let Her 
Go (Alternative Audio).mp3", this file will have:
- artist set to "Passenger"
- title set to "Let Her Go"


### Installation instruction

Install [mutagen](https://mutagen.readthedocs.io/en/latest/):

- for windows run: `pip install mutagen` 

- for linux run: `sudo apt-get install python-mutagen python3-mutagen`


### Usage
1) Open `tag_mp3.py` with your favourite editor and edit directory variable to the directory where 
your audio files are stored.

2) Run the following script:

- for windows: `python .\tag_mp3.py`

- for linux: `python3 tag_mp3.py`


The script has been tested on Ubuntu 18.04 LTS and Windows 10.
