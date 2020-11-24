#!/usr/bin/python3

class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File format")

        self.filename = filename

    #def play(self):
    #    print("playing {} as {}".format(self.filename, self.ext))


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("playing {} as {}".format(self.filename, self.ext))

class OggFile(AudioFile):
    ext = "ogg"
    
    def play(self):
        print("playing {} as {}".format(self.filename, self.ext))
class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("playing {} as {}".format(self.filename, self.ext))
