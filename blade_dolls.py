import pygame as pg
import serial
import time
import os

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

pinAssign = ['mouse_bite', 'mouse_tail', 'cat_bite',
    'cat_claw', 'octo_bite', 'octo_tentacle', 'girl_bite',
    'girl_nipple', 'girl_pussy']

soundDict = {
    'mouse_bite': {
        'mouse_tail': ['squeaky kiss.wav'],
        'cat_bite': ['cat bite.wav', 'squeaky rat.wav'],
        'cat_claw': ['cat scratch.wav', 'rat squeak.wav'],
        'octo_bite': ['water churn.wav', 'squeaky kiss.wav'],
        'octo_tentacle': ['tent squish.wav', 'dog toy squish.wav'],
        'girl_bite': ['kiss.wav', 'girl kiss.wav'],
        'girl_nipple': ['nipple giggle.wav', 'squeaky kiss.wav'],
        'girl_pussy': ['girl resistant moan.wav', 'laughingmice.wav']
    },
    'mouse_tail': {
        'cat_bite': ['cat bite.wav', 'squeaky rat.wav'],
        'cat_claw': ['cat scratch.wav', 'rat squeak.wav'],
        'octo_bite': ['octo whimper.wav', 'squeaky rat.wav'],
        'octo_tentacle': ['clown-teehee.wav', 'dog toy squish.wav'],
        'girl_bite': ['chomp.wav'],
        'girl_nipple': ['girl gasp.wav'],
        'girl_pussy': ['girl scream rat tail.wav', 'rat squeak.wav'],
    },
    'cat_bite': {
        'cat_claw': ['long purr.wav'],
        'octo_bite': ['cat slurp.wav', 'water churn.wav'],
        'octo_tentacle': ['cat bite.wav', 'octo whimper.wav'],
        'girl_bite': ['kiss breath.wav', 'light purr.wav'],
        'girl_nipple': ['nipple giggle.wav', 'kitten meow.wav'],
        'girl_pussy': ['meow commercial.wav'],
    },
    'cat_claw': {
        'octo_bite': ['tom cat.wav', 'octo roar.wav'],
        'octo_tentacle': ['puking or fighting.wav', 'cat scream.wav'],
        'girl_bite': ['throat clearing.wav', 'kitten meow.wav'],
        'girl_nipple': ['girl ouch.wav', 'cat meow.wav'],
        'girl_pussy': ['girl gasp.wav', 'tom cat.wav'],
    },
    'octo_bite': {
        'octo_tentacle': ['bubbles.wav'],
        'girl_bite': ['kiss.wav', 'girl kiss.wav'],
        'girl_nipple': ['girl resistant moan.wav', 'cat slurp.wav'],
        'girl_pussy': ['song easter egg.wav', 'water churn.wav'],
    },
    'octo_tentacle': {
        'girl_bite': ['girl gasp.wav', 'cat_licking.wav'],
        'girl_nipple': ['surprise moan girl.wav', 'water splash.wav'],
        'girl_pussy': ['dubstep porn loop.wav'],
    },
    'girl_bite': {
        'girl_nipple': ['nipple giggle.wav'],
        'girl_pussy': ['girl kiss.wav'],
    },
    'girl_nipple': {
        'girl_pussy': ['temple bell.wav'],
    },
}

def checkifComplete(channel):
    while channel.get_busy():
        pg.time.wait(800)
    channel.stop()

def setup_mixer():
    freq = 48000
    bitsize = -16
    channels = 2
    buffer = 2048
    pg.mixer.init(freq, bitsize, channels, buffer)
    pg.init()
    pg.mixer.set_num_channels(50)

def get_filepath(file):
    return os.path.join(os.getcwd(), file)

def play_sounds(song_array):
    for song in song_array:
        channel = pg.mixer.find_channel(True)
        print "Playing audio : ", song
        sound = pg.mixer.Sound(get_filepath(song))
        sound.set_volume(1)
        channel.play(sound)

def find_and_play_sounds(x, y):
    print x, y
    return play_sounds(soundDict[pinAssign[x]][pinAssign[y]])

if __name__ == "__main__":
    #set up the mixer
    setup_mixer()
    while True :
        state = ser.readline()
        if state:
            x, y = state.split(' ')
            print state
            find_and_play_sounds(int(x), int(y))
