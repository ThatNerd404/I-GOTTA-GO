from Settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.offset = pygame.Vector2()
    def draw(self, surface, target_pos):
        self.offset.x = -(target_pos[0] - Window_Width / 2)
        self.offset.y = -(target_pos[1] - Window_Height / 2)
        for sprite in self:
            surface.blit(sprite.image, sprite.rect.topleft + self.offset)