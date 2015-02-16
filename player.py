import pygame, sys, math
from pygame.locals import *
all_chars = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, image, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        #self.baseimage = pygame.transform.rotate(image.convert_alpha(), 90)  # transparent image
        self.baseimage = image.convert_alpha()
        self.image = self.baseimage
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.items = []
        self.direction = 0 #direction in degrees
        pygame.sprite.Sprite.__init__(self, all_chars)
    
    def update(self, keyPressed):
        self.move(keyPressed)
    
    def move(self, key):
        w = 7.5 #angular speed #actually an omega, you just can't tell
        v = 4 #speed
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
        
