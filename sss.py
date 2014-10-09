#!/usr/bin/python
import serial
import time
import threading
import pygame
from  pygame.locals import *
from sys import exit

ser = serial.Serial(7,9600)
def mypygame():
    pygame.init()
    screen = pygame.display.set_mode((640,480),0,32)
    screen.fill((0,0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(1)
def TXD():
    while True:
        time.sleep(2)
        ser.write("\x41")
def RXD():
    while True:
        print ser.read()

#ser.open()
t1 = threading.Thread(target = TXD, name = "fasong")
t2 = threading.Thread(target = RXD, name = "jiesou")
t3 = threading.Thread(target = mypygame, name = "mypygame")
t1.start()
t2.start()
#t3.start()
t1.join()
#t3.join()
t2.join()
