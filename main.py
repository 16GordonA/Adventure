import pygame, sys, random, time

from player import *
from Item import *


bh = 50 #bonus height for inventory

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 + bh

size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)

charpic = pygame.image.load('player.png')
background = pygame.image.load('background.png')
player = Player(charpic, 250, 250)

while True:
    screen.blit(background, (0, 0+bh))
    all_chars.draw(screen)
    
    key = pygame.key.get_pressed()
    player.update(key)
    
    pygame.display.update()
    pygame.event.pump()
