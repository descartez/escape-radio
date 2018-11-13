from pygame import mixer

sound_filepath = "/home/pi/Desktop/escape-radio/sounds/"
sound_files = []
message_sound = ""

mixer.init()
mixer.music.load(sound_filepath + "Louis Armstrong 1.mp3")
mixer.music.play()