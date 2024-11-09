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
    display_surface = pygame.display.set_mode((Window_Width, Window_Height))
    display_surface.fill('light blue') 
    
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
        display_surface.fill('light blue')
        
        #? draw player on screen
        pygame.draw.circle(display_surface, "red", player_pos, 40)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_pos.y -= 600 * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_pos.y += 600 * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_pos.x -= 600 * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_pos.x += 600 * dt

        pygame.display.update() #* or .flip as flip does only a part of the display while .update does the entire display
        
        #? limits the frame rate to 60
        dt = clock.tick(60) / 1000

    #? closes game properly
    pygame.quit()

if __name__ == "__main__":
    main()