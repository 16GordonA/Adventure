import pygame, sys, math
from pygame.locals import *
from Item import *
all_chars = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, image, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.baseimage = image.convert_alpha()
        self.image = self.baseimage
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.items = []
        self.itemCount = []
        self.direction = 0 #direction in degrees
        pygame.sprite.Sprite.__init__(self, all_chars)
    
    def update(self, keyPressed):
        self.move(keyPressed)
    
    def move(self, key):
        w = 7.5 #angular speed #actually an omega, you just can't tell
        v = 4   #speed
        r = 10  #reach distance
        if key[K_LEFT]:
            self.direction = (self.direction - w)%360
            self.image = pygame.transform.rotate(self.baseimage, -self.direction)
        elif key[K_RIGHT]:
            self.direction = (self.direction + w)%360
            self.image = pygame.transform.rotate(self.baseimage, -self.direction)
        elif key[K_UP]:
            self.rect = self.rect.move(v*math.sin(self.direction *2*math.pi/360), -v*math.cos(self.direction *2*math.pi/360))
        elif key[K_DOWN]:
            self.rect = self.rect.move(-v*math.sin(self.direction *2*math.pi/360), v*math.cos(self.direction *2*math.pi/360))
        elif key[K_SPACE]:
            pointx = (self.rect.right + self.rect.left)/2 + r*math.sin(self.direction *2*math.pi/360) 
            pointy = (self.rect.top + self.rect.bottom)/2 - r*math.cos(self.direction *2*math.pi/360)
            for item in all_items:
                if pointx < item.rect.right + 5 and pointx > item.rect.left - 5:
                    if pointy > item.rect.top - 5 and pointy < item.rect.bottom + 5:
                        self.openChest(item)
    
    def openChest(self, chest):
        for i in range(len(chest.itemTypes)):
            for j in range(chest.contents[i]):
                self.addItem(chest.itemTypes[i])
                
        all_items.remove(chest)
        for i in range(len(self.itemCount)):
            print str(self.itemCount[i])  + self.items[i]
    
    def addItem(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.itemCount[i] += 1
                return
            
        self.items = self.items + [item]
        self.itemCount = self.itemCount + [1]
        
    def hasItem(self, item): #returns index of item or -1
        for i in range(len(self.items)):
            if self.items[i] == item:
                return i
        return -1
        
        
