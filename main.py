import pygame, sys, random, time

from player import *
from Item import *


bh = 60 #bonus height for inventory

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 + bh

size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)

pygame.font.init()
myFont = pygame.font.SysFont("Arial", 10)

charpic = pygame.image.load('player.png')
background = pygame.image.load('background.png')
header = pygame.image.load('header.png')
items = ['wood', 'stone', 'metal', 'glass', 'gems', 'keys']
itempics = ['' for i in range(len(items))]

for i in range(len(items)):
    itempics[i] = pygame.image.load('Resources/' + items[i] + '.png')

rChest = pygame.image.load('chest1.png') #resources
eChest = pygame.image.load('chest2.png') #equipment
iChest = pygame.image.load('chest3.png') #items
table1 = pygame.image.load('CraftingTable1.png') #first table
player = Player(charpic, 250, 250)

#chest = ResourceChest(rChest, 3, 100, 100)
l = Location(eChest, background, 100, 100)
hotspots1 = [[25,225,25,225], [300,500,25,225], [575,775,25,225], [25,225, 325, 525], [575,775,325,525]]
ct = CraftingTable(iChest, table1, 400, 400, hotspots1, ['Jewelry', 'green', 'yellow', 'stick', 'purple'])
for i in range(0,15):
    h = Helper(charpic, random.randint(50,750), random.randint(50 + bh,550 + bh))
numChests = 100
chestLevel = 3
chests = numChests
mainmap = player.mainmap
loc = player.loc

while True:
    while player.mainmap:
        if chests < 1:
            chestLevel += 1
            for i in range(numChests):
                chest = ResourceChest(rChest, chestLevel, random.randint(50, 750), random.randint(50+bh, 550+bh))
        chests = len(all_chests)
        screen.blit(header, (0,0))
        screen.blit(background, (0, 0+bh))
        
        counter = 0
        i = 0
        for it in items:
            a = player.hasItem(it)
            #print player.items
            if a > 0:
                screen.blit(itempics[i], (20 + 60*counter, 40 - itempics[i].get_height()))
                itemcont = myFont.render(str(Player.itemCount[a]) + "x "  + Player.items[a], 1, (255, 255, 255))
                screen.blit(itemcont, (20 + 60*counter, 45))
                counter += 1
            i += 1
        
        all_chars.draw(screen)
        all_items.draw(screen)
        all_chests.draw(screen)
        all_locs.draw(screen)
        
        key = pygame.key.get_pressed()
        for p in all_chars:
            p.update(key)
        
        pygame.display.update()
        pygame.event.pump()
    #when at a specific location
    screen.blit(header, (0,0))
    screen.blit(player.loc.bigImage, (0, 0+bh))
    
    counter = 0
    i = 0
    for it in items:
        a = player.hasItem(it)
        #print player.items
        if a > 0:
            screen.blit(itempics[i], (20 + 60*counter, 40 - itempics[i].get_height()))
            itemcont = myFont.render(str(player.itemCount[a]) + "x "  + player.items[a], 1, (255, 255, 255))
            screen.blit(itemcont, (20 + 60*counter, 45))
            counter += 1
        i += 1
    
    key = pygame.key.get_pressed()
    player.update(key)
    
    if pygame.mouse.get_pressed()[0]:
        player.loc.registerClick()
        time.sleep(.1)
    
    pygame.display.update()
    pygame.event.pump()
    
