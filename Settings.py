import pygame
from os import walk
from os.path import join
import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame
Window_Width, Window_Height = 800, 600
Tile_Size = 32
Crt_On = True
FrameRate = 60 
#? importing 
Snowball_Surf = pygame.image.load("Assets\Img\Snowball_Projectile.png")
Flamingo_Enemy_Surf = pygame.image.load("Assets\Img\Enemy_Flamingo.png")  
pygame.mixer.init() 
Snowball_Sound_Effect = pygame.mixer.Sound("Assets\Sound\Snowball_Sound_Effect.mp3")
Background_Music = "Assets\Sound\Jingle_Bells_Chiptune_Version.mp3"

VIRTUAL_RES = (800, 600)
REAL_RES = (1280, 768)