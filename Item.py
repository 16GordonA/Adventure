import pygame, sys, math, random
from pygame.locals import *
from player import *
all_items = pygame.sprite.Group()
all_chests = pygame.sprite.Group()
all_locs = pygame.sprite.Group()

class Item(pygame.sprite.Sprite):
    def __init__ (self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect().move(x, y)
        pygame.sprite.Sprite.__init__(self, all_items)
    

class ResourceChest(Item):
    resources = ['wood', 'stone', 'metal', 'glass', 'gems']
    
    def __init__ (self, image, level, x, y):
        self.level = level
        self.contents = [random.randint(0,level) for i in range(len(ResourceChest.resources))]
        self.itemTypes = ResourceChest.resources
        if random.randint(0,100) < level:
            self.contents += [1]
            self.itemTypes += ['keys']
        Item.__init__(self, image, x, y)
        all_items.remove(self)
        pygame.sprite.Sprite.__init__(self,all_chests)
        
class Location(pygame.sprite.Sprite):
    
    xmin = 0
    xmax = 1
    ymin = 2
    ymax = 3
    
    def __init__(self, image, bigImage, x, y):
        self.image = image
        self.bigImage = bigImage
        self.hotspots = [[0,0,0,0]] #xmin, xmax, ymin, ymax
        self.items = [None]
        self.action = ''
        self.rect = self.image.get_rect().move(x,y)
        pygame.sprite.Sprite.__init__(self, all_locs)

class CraftingTable(Location):        
    def __init__(self, image, bigImage, x, y, hotspots, items):
        Location.__init__(self, image, bigImage, x, y)
        self.hotspots = hotspots
        self.items = items
    
    def registerClick(self):
        
        xpos = pygame.mouse.get_pos()[0]
        ypos = pygame.mouse.get_pos()[1]
        
        for i in range(len(self.hotspots)):
            if xpos < self.hotspots[i][Location.xmax] and xpos > self.hotspots[i][Location.xmin]:
                if ypos < self.hotspots[i][Location.ymax] and ypos > self.hotspots[i][Location.ymin]:
                    self.action = self.items[i]
                    self.takeAction()
    
    def takeAction(self):
        print self.action
        self.action = ''
                    
        
    