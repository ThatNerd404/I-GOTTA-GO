import pygame
from pygame.locals import *
import sys
from pytmx.util_pygame import load_pygame
from crt_shader import Graphic_engine

from Settings import *
from Enemy import Enemy
from Player import Player_Character
from Game_Logic import *



class Game():
    def __init__(self):
        #? setup pygame
        pygame.init()
        
        #? Main Loop Variables
        self.On_Title_Card = True
        self.Game_Paused = False
        self.Game_Running = True
        
       
        
        #? you need to give your display OPENGL flag to blit screen using OPENGL 
        #! set mode comes first asshole
        pygame.display.set_mode(REAL_RES, DOUBLEBUF|OPENGL)
        
        #? screen size and screen image and junk 
        self.screen = pygame.Surface(VIRTUAL_RES).convert((255, 65282, 16711681, 0)) #! no clue what the .convert does but when removed it doesn't work so...
        
        #? setting up first level
        self.setup('Assets\Maps\Level_1.tmx')
        
        #? init shader class
        self.crt_shader =  Graphic_engine(self.screen)
        snowman_icon = pygame.image.load("Assets\Img\icons8-snowman-32.png")
        pygame.display.set_caption("Summer In December!!!")
        pygame.display.set_icon(snowman_icon)
        self.clock = pygame.time.Clock()

        #? setting up sprites
        
        
        self.player_sprite = Player_Character((Window_Width / 2, Window_Height / 2), all_sprites, collision_sprites)
        #*self.flamingo_sprite = Enemy(Flamingo_Enemy_Surf,(300, 500), (all_sprites, enemy_sprites))
        
    def setup(self,map_link):
        map = load_pygame(map_link)
        for obj in map.get_layer_by_name('Ground'):
            obj.x, obj.y = int(obj.x), int(obj.y)
            obj.width, obj.height = int(obj.width), int(obj.height)
            CollisionSprites((obj.x, obj.y), pygame.Surface((obj.width , obj.height)), collision_sprites)
        for x,y, image in map.get_layer_by_name('Background').tiles():
            Sprite((x * Tile_Size,y * Tile_Size), image, all_sprites)
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
            #! rememeber use self.crt_shader not pygame.display.update()
            #! treat window like it is in 800 by 600 display (even though its not)
            self.crt_shader()
    
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
        title_card = pygame.transform.scale(title_card,(800,600))
        title_card_rect  = title_card.get_frect(center = (Window_Width / 2, Window_Height / 2))

        title_card2 = pygame.image.load("Assets\Img\Title_Card2.png").convert_alpha()
        title_card2 = pygame.transform.scale(title_card2,(800,600))
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
        

            self.crt_shader() #* or .flip as flip does only a part of the display while .update does the entire display
    
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
            #*        elif pygame.key.get_pressed()[pygame.K_1]:
            #*            Crt_On = not Crt_On
            self.crt_shader() #* add this back later when I figure out how to change a variable in another file

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

