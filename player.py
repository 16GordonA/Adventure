import pygame, sys, math
from pygame.locals import *
from Item import *
from imaplib import Response_code
all_chars = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, image, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.baseimage = image.convert_alpha()
        self.image = self.baseimage
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.items = ['null']
        self.itemCount = [0]
        self.direction = 0 #direction in degrees
        self.auto = False
        pygame.sprite.Sprite.__init__(self, all_chars)
    
    def update(self, keyPressed):
        if keyPressed[K_a]:
            self.auto = not self.auto
        if self.auto:
            chests = [item for item in all_items]
            self.move(self.autoMove(chests, keyPressed))
        else:
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
    
    def autoMove(self, chests, key):
        
        if(len(chests)) == 0:
            return key
        
        d = self.distance(chests[0])
        index = 0
        i = 0
        for chest in chests:
            if self.distance(chest) < d:
                d = self.distance(chest)
                index = i
            i += 1
        target = chests[index]
        
        y = -(target.rect.centery - self.rect.centery)
        x = target.rect.centerx - self.rect.centerx
        
        if y == 0:
            if x > 0:
                theta = 90
            elif x < 0: 
                theta = 270
        if y > 0:
            theta = (180*math.atan(x/y)/math.pi) % 360
        if y < 0:
            theta = (180*math.atan(x/y)/math.pi - 180) % 360
       
        resp = [] 
        for b in key:
            resp += [False]
        t = 4 #angle tolerance
        
        if theta - self.direction > t:
            resp[K_RIGHT] = True
            return resp
        if self.direction - theta > t:
            resp[K_LEFT] = True
            return resp
        if self.distance(target) < 10:
            resp[K_SPACE] = True
            return resp
        
        resp[K_UP] = True
        return resp
        
    def distance(self, target):
        y = target.rect.centery - self.rect.centery
        x = target.rect.centerx - self.rect.centerx
        
        return math.sqrt(x*x + y*y)
        
    def openChest(self, chest):
        for i in range(len(chest.itemTypes)):
            for j in range(chest.contents[i]):
                self.addItem(chest.itemTypes[i])
                
        all_items.remove(chest)
    def addItem(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.itemCount[i] += 1
                return
            
        self.items = self.items + [item]
        self.itemCount = self.itemCount + [1]
        
    def hasItem(self, item): #returns index of item or -1
        i = 0
        for it in self.items:
            if it == item:
                return i
            i += 1 
        
        return -1
        
        
