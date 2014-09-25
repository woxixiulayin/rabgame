__author__ = 'gang'

import math
import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from random import randint
SCREEN = (640, 480)
w = SCREEN[0]
h = SCREEN[1]

pygame.init()
screen = pygame.display.set_mode(SCREEN, 0, 32)
rabbit_image = pygame.image.load('images/dude.png')
grass = pygame.image.load('images/grass.png')
castle = pygame.image.load('images/castle.png')

def draw_background():
    for x in range(w / grass.get_width() + 1):
        for y in range(h / grass.get_height() + 1):
            screen.blit(grass, (x * grass.get_width(), y * grass.get_height()))
    screen.blit(castle, (0 , 30))
    screen.blit(castle, (0 , 135))
    screen.blit(castle, (0 , 240))
    screen.blit(castle, (0 , 345))

class RABBIT(object):
    def __init__(self):
        self.position = Vector2(randint(40, w - 40), randint(40 , h -40))
        self.angle = 0
        self.arrows = []

    def draw(self):
        screen.blit(rabbit_image, self.position)

draw_background()
rabbit = RABBIT()
rabbit.draw()
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.value == K_ESCAPE:
                exit()
