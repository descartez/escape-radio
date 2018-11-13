from pygame import mixer
import random

sound_filepath = "/home/pi/Desktop/escape-radio/sounds/"
sound_files = ["Louis Armstrong 1.mp3","Theater Of Hits Oklahoma.mp3"]
message_sound = ""

mixer.init()
mixer.music.load(sound_filepath + sound_files[random.randint(0,(len(sound_files)-1))])
mixer.music.play()