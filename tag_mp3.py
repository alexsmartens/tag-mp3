import os
from mutagen.easyid3 import EasyID3


directory = "/home/alex/Downloads"
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        audio = EasyID3(directory + "/" + filename)

        # Remove mp3 extention
        filename = filename[:-4]
        if filename[0:].find(" -") > 0:
            artist = filename[0:filename.find(" -")]
            title = filename[filename.find(" -") + 3:]
            # Filter titles
            if title[0:].find(" (") > 0:
                title = title[0:title.find(" (")]
            if title[0:].find(" [") > 0:
                title = title[0:title.find(" [")]
            # Update title and artist tags
            audio['title'] = title
            audio['artist'] = artist
            audio.save()

    else:
        print(">> File with a different extention {0}".format(filename))