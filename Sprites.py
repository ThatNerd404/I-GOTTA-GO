from Settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class Player_Character(Sprite):
    def __init__(self,pos, groups, collision_sprites):
        #? setup player sprite and speed and what not
        surf = pygame.Surface((40,80))
        super().__init__(pos, surf,groups)
        self.image = pygame.image.load("Assets\Img\Player\Player_Snowman.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect =  self.image.get_frect(center = pos)
        self.hitbox = self.rect.inflate(-45,-5)
        self.Player_Direction = pygame.math.Vector2(0,0)
        self.gravity = 60
        self.on_floor = False
        #? setup cooldown on snowball launcher
        self.can_shoot = True
        self.snowball_shoot_time = 0
        self.cooldown_duration = 300
        self.Facing_Direction = "Right"
        self.Player_Speed = 300
        self.collision = collision_sprites
                
    def input(self):
    
        #? get the keys that are being pressed 
        Movement_keys = pygame.key.get_pressed()
        jump_key = pygame.key.get_just_pressed()
        self.Player_Direction.x = int(Movement_keys[pygame.K_d] or Movement_keys[pygame.K_RIGHT]) - int(Movement_keys[pygame.K_a] or Movement_keys[pygame.K_LEFT])
        #self.Player_Direction.y = int(Movement_keys[pygame.K_s] or Movement_keys[pygame.K_DOWN]) - int(Movement_keys[pygame.K_w] or Movement_keys[pygame.K_UP] or Movement_keys[pygame.K_SPACE])
        if (jump_key[pygame.K_SPACE] or jump_key[pygame.K_w] or jump_key[pygame.K_UP]) and self.on_floor:
            self.Player_Direction.y = -20
        #self.Player_Direction = self.Player_Direction.normalize() if self.Player_Direction else self.Player_Direction #? makes the speed constant when you click 2 buttons at the same time
        Shooting_keys = pygame.key.get_just_pressed()
        '''if Shooting_keys[pygame.K_q] and self.can_shoot:
            Snowball(Snowball_Surf, self.rect.midright, (all_sprites, snowball_sprites))
            self.can_shoot = False
            self.snowball_shoot_time = pygame.time.get_ticks()
               
        self.snowball_timer()
    
    def snowball_timer(self): 
        if self.can_shoot == False:
            current_time = pygame.time.get_ticks()
            if current_time - self.snowball_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
    '''
    def move(self,dt):
        
        self.hitbox.x += self.Player_Direction.x * self.Player_Speed * dt
        self.collide('Horizontal')
        
        if self.Player_Direction.x == 1:
            self.image = pygame.image.load("Assets\Img\Player\Player_Snowman.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (64,64))
        elif self.Player_Direction.x == -1:
            self.image = pygame.image.load("Assets\Img\Player\Player_Snowman_Backward.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (64,64))
        
        self.Player_Direction.y += self.gravity * dt
        self.hitbox.y += self.Player_Direction.y # * self.Player_Speed * dt
        self.collide('Vertical')
        self.rect.center = self.hitbox.center
        
    def collide(self, direction):
        for sprite in self.collision:
            if sprite.rect.colliderect(self.hitbox):
                if direction == 'Horizontal':
                    if self.Player_Direction.x > 0: 
                        self.hitbox.right = sprite.rect.left
                    elif self.Player_Direction.x < 0: 
                        self.hitbox.left = sprite.rect.right
                elif direction == 'Vertical':
                    if self.Player_Direction.y < 0: self.hitbox.top = sprite.rect.bottom
                    elif self.Player_Direction.y > 0: self.hitbox.bottom = sprite.rect.top
                    self.Player_Direction.y = 0
                #! hey if you pause in the air this counter doesnt stop :)        
    def check_floor(self):

        bottom_rect = pygame.FRect((0,0),(self.rect.width, 2)).move_to(midtop = self.rect.midbottom)
        level_rects = [sprite.rect for sprite in self.collision]
        bottom_rect.collidelist(level_rects)
        self.on_floor = True if bottom_rect.collidelist(level_rects) >= 0 else False
    
    def update(self, dt):
        self.check_floor()
        self.input()
        self.move(dt)
        
    
'''class Snowball(pygame.sprite.Sprite):
    
    def __init__(self,surf,pos,groups):
        super().__init__(groups)
        
        self.image = surf
        self.image = pygame.transform.scale(self.image, (12,12))
        self.rect = self.image.get_frect(midleft = pos)
        
        
    def update(self,dt):
        self.rect.centerx += 400 * dt
        
        #? destroys itself if it leaves the screen
        if self.rect.right > 1280:
            self.kill()    '''

class Enemy(Sprite):
    def __init__(self,pos,groups):
        surf = pygame.Surface((40,80))
        super().__init__(pos, surf,groups)
        self.image = pygame.image.load("Assets\Img\Enemy_Flamingo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_frect(topleft = pos)

class CollisionSprites(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        