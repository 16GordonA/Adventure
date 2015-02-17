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
    def __init__(self, image, bigImage, x, y):
        self.image = image
        self.bigImage = bigImage
        self.rect = self.image.get_rect().move(x,y)
        pygame.sprite.Sprite.__init__(self, all_locs)
    