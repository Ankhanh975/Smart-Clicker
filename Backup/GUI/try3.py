import math
import pygame, sys, time 
from pygame.locals import *

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)
pygame.display.set_caption('follow mouse')
surface.fill((255,255,255))

class Hero():
    def Attack(self):
        surface.fill ((255,255,255))
        amntTuple = pygame.mouse.get_pos()
        #Use pygame.Color to make a color.
        #The last parameter is linewidth, and can be set to 0 for filled circles.
        pygame.draw.circle(surface, pygame.Color(0,0,255), amntTuple, 20, 2)
        #The blit was deleted because it did nothing and the broke code.

var = Hero()
while True:
    for event in pygame.event.get():
            #Add a quit event so you can close your game normally.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    var.Attack()

    #Update once at the end of each gameloop.
    pygame.display.update()