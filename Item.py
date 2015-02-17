import pygame, sys, math, random
from pygame.locals import *
from player import *
all_items = pygame.sprite.Group()

class Item(pygame.sprite.Sprite):
    def __init__ (self, image):
        self.image = image
        pygame.sprite.Sprite.__init__(self, all_items)
    

class ResourceChest(Item):
    resources = ['wood', 'stone', 'metal', 'glass', 'gems']
    
    def __init__ (self, image, level):
        self.level = level
        self.contents = [random.randint(0,level) for i in range(len(ResourceChest.resources))]
        self.itemTypes = ResourceChest.resources
        Item.__init__(self, image)
        
        