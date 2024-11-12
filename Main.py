import pygame
from pygame.locals import *
from Player import Player
import sys

class Game:
    def __init__(self):
        #? setup pygame
        pygame.init()
        Window_Width, Window_Height = 1280, 720

        #? screen size and screen image and junk 
        snowman_icon = pygame.image.load("Assets\Img\icons8-snowman-32.png")
        pygame.display.set_caption("Summer In December!!!")
        pygame.display.set_icon(snowman_icon)
        self.screen = pygame.display.set_mode((Window_Width, Window_Height))
        
        #? setting time for the framerate
        self.clock = pygame.time.Clock()
        
        self.Game_Running = True
        
        #? setting up groups
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self.all_sprites)
        
    def run(self):
        
        #? event loop
        while self.Game_Running:
        
        #? limits the frame rate to 60
            dt = self.clock.tick(60) / 1000
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.Game_Running = False   
    
            self.all_sprites.update(dt)  
    
            #? wipes away last frame
            self.screen.fill('royal blue1')
            self.all_sprites.draw(self.screen)
            pygame.display.update() #* or .flip as flip does only a part of the display while .update does the entire display
            
        #? closes game properly
        pygame.quit()
        sys.exit()
        
        
#? groups of sprites so I don't have to do a bunch of shit yada yada read the docs again moron

#! when making multiple sprites that are the same import once and then use a for loop 
if __name__ == "__main__":
    game = Game()
    game.run()
    
