#!/usr/bin/python
import pygame
import math
from  pygame.locals import *
from sys import exit
import random

circle_image=pygame.image.load("circle1.gif")

def draw_range(x, y, r, n, s):
    x1 = x - r*math.cos(math.radians(n))
    y1 = y + r*math.sin(math.radians(n))
    x2 = x + r*math.cos(math.radians(n))
    y2 = y - r*math.sin(math.radians(n))
    pygame.draw.line(s, red, (x1,y1),(x2,y2),3)

red = (255,0,0)
green = (0,255,0)
r = 85
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
screen.fill((0,0,0))
pygame.draw.circle(screen, red, (160,160), 110, 3)
clock = pygame.time.Clock()


mysurface = pygame.Surface((2*r,2*r))
screen.fill((20,20,10))
pygame.draw.circle(mysurface, green, (r,r), r, 2)
draw_range(r,r,r,45,mysurface)
s=mysurface.convert_alpha()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit(1)
    time_passed_second = clock.tick(30)
    screen.fill((20,20,10))
    screen.blit(pygame.transform.rotozoom(s,0,random.randint(0,100)/100.),(100,100))
    #pygame.draw.circle(screen, green, (160,160), r, 2)
    #draw_range(160,160,r,45)
    pygame.draw.circle(screen, green, (480,160), r, 2)
    draw_range(480,160,r,random.randint(-90,90),screen)
    pygame.display.update()