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
rChest = pygame.image.load('chest1.png') #resources
eChest = pygame.image.load('chest2.png') #equipment
iChest = pygame.image.load('chest3.png') #items
player = Player(charpic, 250, 250)

chest = ResourceChest(rChest, 3, 100, 100)
chests = 1

#player.openChest(chest)

for i in range(len(player.items)):
    print str(player.itemCount[i]) + "x "  + player.items[i]

while True:
    if chests < 1:
        chest = ResourceChest(rChest, 3, random.randint(50, 750), random.randint(50+bh, 550+bh))
        chests = 1
    chests = len(all_items)
    screen.blit(background, (0, 0+bh))
    all_chars.draw(screen)
    all_items.draw(screen)
    
    key = pygame.key.get_pressed()
    player.update(key)
    
    pygame.display.update()
    pygame.event.pump()
