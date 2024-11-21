import pygame
from pygame.locals import *
import sys
from Settings import *
from Enemy import Enemy
from Player import Player_Character

         
class Game():
    def __init__(self):
        #? setup pygame
        pygame.init()
        
        #? Main Loop Variables
        self.On_Title_Card = True
        self.Game_Paused = False
        self.Game_Running = True
        
        
        #? screen size and screen image and junk 
        self.screen = pygame.display.set_mode((Window_Width, Window_Height), pygame.SRCALPHA)
        snowman_icon = pygame.image.load("Assets\Img\icons8-snowman-32.png")
        pygame.display.set_caption("Summer In December!!!")
        pygame.display.set_icon(snowman_icon)
        self.clock = pygame.time.Clock()

        #? setting up sprites
        self.player_sprite = Player_Character((Window_Width / 2, Window_Height / 2), all_sprites)
        self.flamingo_sprite = Enemy(Flamingo_Enemy_Surf,(1000, 384), (all_sprites, enemy_sprites))

    
    def run(self):
        #? Main Game Loop
        while self.Game_Running:
            
            self.title_menu()
            '''nvm just use background_music.play(loops= -1) and it will go infinitly don't forget to use .setvolume tho'''
        
            #? limits the frame rate to 60
            dt = self.clock.tick(60) / 1000

            #? check for exiting and check for pausing
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.Game_Running = False   
                elif event.type == KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_p]:
                        self.Game_Paused = not self.Game_Paused
                        self.pause_menu()
            
            #? updating the screen
            all_sprites.update(dt)  
            self.collisions()
    
            #? wipes away last frame
            self.screen.fill('#639bff')
            all_sprites.draw(self.screen)
            pygame.display.update() #* or .flip as flip does only a part of the display while .update does the entire display
    
    def collisions(self):
        
        player_dies = pygame.sprite.spritecollide(self.player_sprite, enemy_sprites, False, pygame.sprite.collide_mask)
        #? if you die the game ends no shit
        if player_dies:
            self.Game_Running = False
        #? for each snowball if the snowball collides with an enemy sprite kill it
        for snowball in snowball_sprites:
            snowball_hits_enemy =  pygame.sprite.spritecollide(snowball, enemy_sprites, True, pygame.sprite.collide_mask)
            if snowball_hits_enemy:
                Snowball_Sound_Effect.play()
                snowball.kill()   
                
    def title_menu(self):
        title_card = pygame.image.load("Assets\Img\Title_Card1.png").convert_alpha()
        title_card = pygame.transform.scale(title_card,(768,768))
        title_card_rect  = title_card.get_frect(center = (Window_Width / 2, Window_Height / 2))

        title_card2 = pygame.image.load("Assets\Img\Title_Card2.png").convert_alpha()
        title_card2 = pygame.transform.scale(title_card2,(768,768))
        title_card_rect2  = title_card2.get_frect(center = (Window_Width / 2, Window_Height / 2))

        display_interval = 400  # 1 second interval for switching cards
        last_switch_time = pygame.time.get_ticks()
        show_title_card_2 = False

        while self.On_Title_Card:
        #? limits the frame rate to 60
            dt = self.clock.tick(60) / 1000
            self.screen.fill("#639bff")
    
            # Check if it's time to switch the displayed image
            self.screen.blit(title_card, title_card_rect)

            current_time = pygame.time.get_ticks()
            if current_time - last_switch_time >= display_interval:
                show_title_card_2 = not show_title_card_2  # Toggle title card
                last_switch_time = current_time

            # Draw the appropriate title card
            if show_title_card_2:
                self.screen.blit(title_card2, title_card_rect2)
            else:
                self.screen.blit(title_card, title_card_rect)  
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()   
                elif event.type == pygame.KEYDOWN:
                    self.On_Title_Card = False
        

            pygame.display.update() #* or .flip as flip does only a part of the display while .update does the entire display
    
    def pause_menu(self):
        dt = self.clock.tick(60) / 1000
        while self.Game_Paused:
        
            font = pygame.font.Font("Assets\Fonts\\alagard.ttf", 75)
            text = font.render("PAUSED", None, (255, 255, 255))  
            text_rect = text.get_rect(center=(Window_Width // 2, Window_Height // 2))
            self.screen.blit(text, text_rect)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()   
                elif event.type == KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_p]:
                        self.Game_Paused = False
            
            pygame.display.update() #* or .flip as flip does only a part of the display while .update does the entire display

    """Paused_Card = pygame.image.load("Assets\Img\Title_Card1.png").convert_alpha()
    Paused_Card = pygame.transform.scale(Paused_Card,(768,768))
    Paused_Card_rect  = Paused_Card.get_frect(center = (Window_Width / 2, Window_Height / 2))
    """

       
if __name__ == "__main__":
    Game = Game()
    Game.run()
    pygame.quit()
    sys.exit()
        
        
#? groups of sprites so I don't have to do a bunch of shit yada yada read the docs again moron

#! when making multiple sprites that are the same import once and then use a for loop 

