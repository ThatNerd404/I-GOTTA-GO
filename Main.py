import pygame,sys
from pygame.locals import *

def main():
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
    
    #? set up for moving the player
    player_pos = pygame.Vector2(Window_Width / 2, Window_Height / 2)
    #? event loop
    Game_Running = True
    while Game_Running:
        for event in pygame.event.get():
            if event.type == QUIT:
                Game_Running = False   
        
        #? wipes away last frame
        screen.fill('royal blue1')
        
        #? load player and resize
        snowman_player = pygame.image.load("Assets\Img\THE_SNOWMAN.png").convert_alpha() #* apparently adding convert_alpha makes the framerate go up ¯\_(ツ)_/¯
        snowman_player = pygame.transform.scale(snowman_player, (128,128))
        
        #? place player on screen and controls
        screen.blit(snowman_player, player_pos)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]: #* Decreasing y moves you up and Increasing y moves you down 
            player_pos.y -= 600 * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_pos.y += 600 * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: #* Decreasing x moves you left and Increasing x moves you right
            player_pos.x -= 600 * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_pos.x += 600 * dt
            

        pygame.display.update() #* or .flip as flip does only a part of the display while .update does the entire display
        
        #? limits the frame rate to 60
        dt = clock.tick(60) / 1000
        

    #? closes game properly
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()