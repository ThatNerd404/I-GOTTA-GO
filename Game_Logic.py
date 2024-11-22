from Settings import *
import pygame
from pygame.locals import *

class CollisionSprites(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill('red')
        self.rect = self.image.get_frect(center = pos)
        