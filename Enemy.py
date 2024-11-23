import pygame
from pygame.locals import *
from Settings import *
class Enemy(pygame.sprite.Sprite):
    def __init__(self,surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect =  self.image.get_frect(center = pos)
   