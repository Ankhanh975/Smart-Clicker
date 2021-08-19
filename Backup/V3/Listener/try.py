import main
import win32api, win32con
import time
import pygame
clock = pygame.time.Clock()


while True:
	for x in range(256):
        a = win32api.GetKeyState(x)
        if  a==-128 or a==-127:
            print(x)
	print(main.Get())
	clock.tick(60)
