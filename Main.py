import pygame
from pygame.locals import *
import sys
from Settings import *

class Player_Character(pygame.sprite.Sprite):
    def __init__(self, groups):
        #? setup player sprite and speed and what not
        super().__init__(groups)
        self.image = pygame.image.load("Assets\Img\Player_Snowman.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (96,96))
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
            Snowball(Game.Snowball_Surf, self.rect.midright, (Game.all_sprites, Game.snowball_sprites))
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

class Enemy(pygame.sprite.Sprite):
    def __init__(self,surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (96,96))
        self.rect =  self.image.get_frect(center = pos)
            
class Game():
    def __init__(self):
        #? setup pygame
        pygame.init()
        
        #? Main Loop Variables
        self.On_Title_Card = True
        self.Game_Paused = False
        self.Game_Running = True
        
        #? importing 
        self.Snowball_Surf = pygame.image.load("Assets\Img\Snowball_Projectile.png")
        self.Enemy_Surf = pygame.image.load("Assets\Img\Enemy_Flamingo.png")
        pygame.mixer.init()
        self.Snowball_Sound_Effect = pygame.mixer.Sound("Assets\Sound\Snowball_Sound_Effect.mp3")
        #? screen size and screen image and junk 
        self.screen = pygame.display.set_mode((Window_Width, Window_Height), pygame.SRCALPHA)
        snowman_icon = pygame.image.load("Assets\Img\icons8-snowman-32.png")
        pygame.display.set_caption("Summer In December!!!")
        pygame.display.set_icon(snowman_icon)
        self.clock = pygame.time.Clock()

        #? setting up groups
        self.all_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.snowball_sprites = pygame.sprite.Group()
        self.player_sprite = Player_Character(self.all_sprites)
        self.flamingo_sprite = Enemy(self.Enemy_Surf,(1000, 384), (self.all_sprites, self.enemy_sprites))

    
    def run(self):
        while self.Game_Running:
            
            self.title_menu()
            '''nvm just use background_music.play(loops= -1) and it will go infinitly don't forget to use .setvolume tho'''
        
            #? limits the frame rate to 60
            dt = self.clock.tick(60) / 1000
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.Game_Running = False   
                elif event.type == KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_p]:
                        Game_Paused = not Game_Paused
                        self.pause_menu()
            
            #? updating the screen
            self.all_sprites.update(dt)  
            self.collisions()
    
    #? wipes away last frame
            self.screen.fill('#639bff')
            self.all_sprites.draw(self.screen)
            pygame.display.update() #* or .flip as flip does only a part of the display while .update does the entire display
    
    def collisions(self):
    
        player_dies = pygame.sprite.spritecollide(self.player_sprite, self.enemy_sprites, False, pygame.sprite.collide_mask)
    
        if player_dies:
            self.Game_Running = False
         #? for each snowball if the snowball collides with an enemy sprite kill it
        for snowball in self.snowball_sprites:
            snowball_hits_enemy =  pygame.sprite.spritecollide(snowball, self.enemy_sprites, True, pygame.sprite.collide_mask)
            if snowball_hits_enemy:
                self.Snowball_Sound_Effect.play()
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

