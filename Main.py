import pygame
from pygame.locals import *
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        
        #? setup player sprite and speed and what not
        super().__init__(groups)
        self.image = pygame.image.load("Assets\Img\Player_Snowman.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (96,96))
        Window_Width, Window_Height = 1280, 720
        self.rect =  self.image.get_frect(center = (Window_Width / 2, Window_Height / 2))
        self.Player_Direction = pygame.math.Vector2(0,0)
        
        #? setup cooldown on snowball launcher
        self.can_shoot = True
        self.snowball_shoot_time = 0
        self.cooldown_duration = 300
        self.Facing_Direction = "Right"
        
    def update(self, dt):
        
        self.Player_Speed = 800
        
        #? get the keys that are being pressed 
        Movement_keys = pygame.key.get_pressed()
        self.Player_Direction.x = int(Movement_keys[pygame.K_d] or Movement_keys[pygame.K_RIGHT]) - int(Movement_keys[pygame.K_a] or Movement_keys[pygame.K_LEFT])
        self.Player_Direction.y = int(Movement_keys[pygame.K_s] or Movement_keys[pygame.K_DOWN]) - int(Movement_keys[pygame.K_w] or Movement_keys[pygame.K_UP] or Movement_keys[pygame.K_SPACE])
        
        self.Player_Direction = self.Player_Direction.normalize() if self.Player_Direction else self.Player_Direction #? makes the speed constant when you click 2 buttons at the same time
        self.rect.center += self.Player_Direction * self.Player_Speed * dt
        
        Shooting_keys = pygame.key.get_just_pressed()
        if Shooting_keys[pygame.K_q] and self.can_shoot:
            Snowball(Snowball_Surf, self.rect.midright, all_sprites)
            self.can_shoot = False
            self.snowball_shoot_time = pygame.time.get_ticks()
               
        self.snowball_timer()
        
        
        
             
    def snowball_timer(self): 
        if self.can_shoot == False:
            current_time = pygame.time.get_ticks()
            if current_time - self.snowball_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

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

#? setup pygame
pygame.init()
Window_Width, Window_Height = 1280, 720

#? screen size and screen image and junk 
snowman_icon = pygame.image.load("Assets\Img\icons8-snowman-32.png")
pygame.display.set_caption("Summer In December!!!")
pygame.display.set_icon(snowman_icon)
screen = pygame.display.set_mode((Window_Width, Window_Height))
        
#? setting time for the framerate
clock = pygame.time.Clock()
Game_Running = True
        
#? setting up groups
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)
        
Snowball_Surf = pygame.image.load("Assets\Img\Snowball_Projectile.png")


#? event loop
while Game_Running:
        
        #? limits the frame rate to 60
    dt = clock.tick(60) / 1000
        
    for event in pygame.event.get():
        if event.type == QUIT:
            Game_Running = False   
    
    all_sprites.update(dt)  
    
    #? wipes away last frame
    screen.fill('royal blue1')
    all_sprites.draw(screen)
    pygame.display.update() #* or .flip as flip does only a part of the display while .update does the entire display
            
#? closes game properly
pygame.quit()
sys.exit()
        
        
#? groups of sprites so I don't have to do a bunch of shit yada yada read the docs again moron

#! when making multiple sprites that are the same import once and then use a for loop 

