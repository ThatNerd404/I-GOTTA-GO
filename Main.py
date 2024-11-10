import pygame
from pygame.locals import *
from Player import Player
import sys


#? setup pygame
pygame.init()
    
#? screen size and screen image and junk 
snowman_icon = pygame.image.load("Assets\Img\icons8-snowman-32.png")
Window_Width, Window_Height = 1280, 720
pygame.display.set_caption("Summer In December!!!")
pygame.display.set_icon(snowman_icon)
screen = pygame.display.set_mode((Window_Width, Window_Height))
screen.fill('royal blue1') 
    
#? setting time for the framerate
clock = pygame.time.Clock()
dt = 0
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

    
#? event loop
Game_Running = True
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
    
