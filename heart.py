__author__ = 'gang'

import math
import pygame
from pygame.locals import*

def fun1(x):
    y = math.sqrt(1 - (abs(x)-1)**2)
    return y

def fun2(x):
    y = math.acos(1 - abs(x)) - math.pi
    return  y

w, h = 1000, 800
screen = pygame.display.set_mode((w,h), 0, 32)
screen.fill((255, 255, 255))

x0 = w / 2
y0 = h / 3


point = []

def draw_point(x, y):
    pygame.draw.circle(screen, (255, 0, 255), (x , y), 1)


l = range(-200, 200)
def xfun():
    for x in l:
        point.append((x + x0, int(0 - fun1(x / 100.)*100) + y0))
    for x in l[-1:1:-1]:
        point.append((x + x0, int(0 - fun2(x / 100.)*100) + y0))


xfun()

pygame.draw.polygon(screen,(255,100,100),point)
#for x in point:
  #  draw_point(x[0],x[1])
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()