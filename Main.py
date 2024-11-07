import pygame, sys
from pygame.locals import *

def main():
    #? setup pygame
    pygame.init()
    
    #? screen size and the clock which has the frames and stuff to create the game loop
    screen = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()
    pygame.display.set_caption("I GOTTA GO!!!")
    
    #? checks if you end the game
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()