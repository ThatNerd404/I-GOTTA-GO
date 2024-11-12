import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("Assets\Img\Player_Snowman.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (128,128))
        Window_Width, Window_Height = 1280, 720
        self.rect =  self.image.get_frect(center = (Window_Width / 2, Window_Height / 2))
        self.Player_Speed = 300
        self.Player_Direction = pygame.math.Vector2(0,0)
        
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.Player_Direction.x = int(keys[pygame.K_d] or keys[pygame.K_RIGHT]) - int(keys[pygame.K_a] or keys[pygame.K_LEFT])
        self.Player_Direction.y = int(keys[pygame.K_s] or keys[pygame.K_DOWN]) - int(keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE])
        
        if self.Player_Direction.x == 1:
            self.image = pygame.image.load("Assets\Img\Player_Snowman.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (128,128))
        
        elif self.Player_Direction.x == -1:
            self.image = pygame.image.load("Assets\Img\Player_Snowman_Backward.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (128,128))
        
        self.Player_Direction = self.Player_Direction.normalize() if self.Player_Direction else self.Player_Direction #? makes the speed constant when you click 2 buttons at the same time
        self.rect.center += self.Player_Direction * self.Player_Speed * dt
