#!/usr/bin/python
import serial
import time
import threading
import pygame
import math
from  pygame.locals import *
from sys import exit

ser = serial.Serial(11,9600)

def draw_range(x, y, r, n):
    x1 = x - r*math.cos(math.radians(n))
    y1 = y + r*math.sin(math.radians(n))
    x2 = x + r*math.cos(math.radians(n))
    y2 = y - r*math.sin(math.radians(n))
    pygame.draw.line(screen, red, (x1,y1),(x2,y2),5)

def mypygame():
    red = (0,255,0)
    pygame.init()
    screen = pygame.display.set_mode((640,480),0,32)
    screen.fill((0,0,0))
    pygame.draw.circle(screen, red, (160,160), 110, 3)
    draw_range(160,160,110,45)
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
#t1 = threading.Thread(target = TXD, name = "fasong")
#t2 = threading.Thread(target = RXD, name = "jiesou")
t3 = threading.Thread(target = mypygame, name = "mypygame")
#t1.start()
#t2.start()
t3.start()
#t1.join()
t3.join()
#t2.join()
