from RPi import GPIO
from time import sleep
from pygame import mixer
import random

sound_filepath = "/home/pi/Desktop/escape-radio/sounds/"
sound_files = ["A Man Called X - Five Ounces Of Treason.mp3","Sherlock Holmes - The Retired Colourman.mp3", "Suspense - The Hitchiker.mp3", "The Shadow - Murder in the Death House.mp3"]
message_sound = "secret message.mp3"

clk = 17
dt = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)


counter = 0
upper_bound = 20
lower_bound = 0
clkLastState = GPIO.input(clk)

mixer.init()


try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                sleep(0.01)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                                if counter >= upper_bound:
                                    counter = upper_bound
                        if dtState == clkState:
                                counter -= 1
                                if counter <= lower_bound:
                                    counter = lower_bound
                        if counter < 5 and counter >= 0:
                                mixer.music.load(sound_filepath + sound_files[0])
                        if counter >= 5 and counter <= 8:
                                mixer.music.load(sound_filepath + sound_files[1])
                        if counter > 8 and counter <= 11:
                                mixer.music.load(sound_filepath + message_sound)
                        if counter > 11 and counter <= 14:
                                mixer.music.load(sound_filepath + sound_files[2])
                        if counter > 14 and counter <= 20:
                                mixer.music.load(sound_filepath + sound_files[3])
                        print(counter)
                        mixer.music.play()
        
                clkLastState = clkState
                
finally:
        GPIO.cleanup()