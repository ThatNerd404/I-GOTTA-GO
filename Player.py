import pygame
from pygame.locals import *
from Settings import *


class Player_Character(pygame.sprite.Sprite):
    def __init__(self,pos, groups, collision_sprites):
        #? setup player sprite and speed and what not
        super().__init__(groups)
        self.image = pygame.image.load("Assets\Img\Player_Snowman.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect =  self.image.get_frect(center = pos)
        self.hitbox = self.rect.inflate(-15,-10)
        self.Player_Direction = pygame.math.Vector2(0,0)
        
        #? setup cooldown on snowball launcher
        self.can_shoot = True
        self.snowball_shoot_time = 0
        self.cooldown_duration = 300
        self.Facing_Direction = "Right"
        self.Player_Speed = 300
        self.collision = collision_sprites
        
    def input(self):
    
        #? get the keys that are being pressed 
        Movement_keys = pygame.key.get_pressed()
        self.Player_Direction.x = int(Movement_keys[pygame.K_d] or Movement_keys[pygame.K_RIGHT]) - int(Movement_keys[pygame.K_a] or Movement_keys[pygame.K_LEFT])
        self.Player_Direction.y = int(Movement_keys[pygame.K_s] or Movement_keys[pygame.K_DOWN]) - int(Movement_keys[pygame.K_w] or Movement_keys[pygame.K_UP] or Movement_keys[pygame.K_SPACE])
        
        self.Player_Direction = self.Player_Direction.normalize() if self.Player_Direction else self.Player_Direction #? makes the speed constant when you click 2 buttons at the same time
        Shooting_keys = pygame.key.get_just_pressed()
        if Shooting_keys[pygame.K_q] and self.can_shoot:
            Snowball(Snowball_Surf, self.rect.midright, (all_sprites, snowball_sprites))
            self.can_shoot = False
            self.snowball_shoot_time = pygame.time.get_ticks()
               
        self.snowball_timer()
    
    def snowball_timer(self): 
        if self.can_shoot == False:
            current_time = pygame.time.get_ticks()
            if current_time - self.snowball_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
    
    def move(self,dt):
        
        self.hitbox.x += self.Player_Direction.x * self.Player_Speed * dt
        self.collide('Horizontal')
        self.hitbox.y += self.Player_Direction.y * self.Player_Speed * dt
        self.collide('Vertical')
        self.rect.center = self.hitbox.center
        
    def collide(self, direction):
        for sprite in self.collision:
            if sprite.rect.colliderect(self.hitbox):
                if direction == 'Horizontal':
                    if self.Player_Direction.x > 0: self.hitbox.right = sprite.rect.left
                    elif self.Player_Direction.x < 0: self.hitbox.left = sprite.rect.right
                elif direction == 'Vertical':
                    if self.Player_Direction.y < 0: self.hitbox.top = sprite.rect.bottom
                    elif self.Player_Direction.y > 0: self.hitbox.bottom = sprite.rect.top
    
    def update(self, dt):
        self.input()
        self.move(dt)
        
    
class Snowball(pygame.sprite.Sprite):
    
    def __init__(self,surf,pos,groups):
        super().__init__(groups)
        
        self.image = surf
        self.image = pygame.transform.scale(self.image, (12,12))
        self.rect = self.image.get_frect(midleft = pos)
        
        
    def update(self,dt):
        self.rect.centerx += 400 * dt
        
        #? destroys itself if it leaves the screen
        if self.rect.right > 1280:
            self.kill()    