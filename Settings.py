import pygame
Window_Width, Window_Height = 1280, 768
Tile_Size = 64
#? importing 
Snowball_Surf = pygame.image.load("Assets\Img\Snowball_Projectile.png")
Enemy_Surf = pygame.image.load("Assets\Img\Enemy_Flamingo.png")  
pygame.mixer.init() 
Snowball_Sound_Effect = pygame.mixer.Sound("Assets\Sound\Snowball_Sound_Effect.mp3")
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
snowball_sprites = pygame.sprite.Group()