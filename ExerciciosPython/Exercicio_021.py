'''Faça um programa em Python que abra e reproduza o
áudio de um arquivo MP3.'''

from pygame import *

mixer.init()
mixer.music.load("Exercicio_021.mp3")
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)