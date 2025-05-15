import pygame


class Pessoa(pygame.sprite.Sprite):
    def __init__(self, img_personagem,start_x,start_y, blocks,spikes,screen_width, screen_height):
        super().__init__()
        self.original_image = img_personagem
        self.image = img_personagem
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-20, -20)

        self.speedx = 0
        self.speedy = 0
        self.jump_force = -15
        self.gravity = 1
        self.isJump = False
        self.blocks = blocks
        self.WIDTH = screen_width
        self.HEIGHT = screen_height
    
        self.spikes = spikes
        self.facing_right = True
        self.morto = False
        self.rect.x = start_x
        self.rect.y = start_y

    def update(self):
        # Direção
        if self.speedx > 0:
            self.facing_right = True
        elif self.speedx < 0:
            self.facing_right = False

        self.image = pygame.transform.flip(self.original_image, True, False) if self.facing_right else self.original_image

        # Movimento horizontal
        self.rect.x += self.speedx
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in collisions:
            if self.speedx > 0:
                self.rect.right = block.rect.left
            elif self.speedx < 0:
                self.rect.left = block.rect.right

        # Movimento vertical (gravidade)
        self.speedy += self.gravity
        self.rect.y += self.speedy
        on_ground = False

        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in collisions:
            if self.speedy > 0:  # Caindo
                self.rect.bottom = block.rect.top
                self.speedy = 0
                on_ground = True
            elif self.speedy < 0:  # Subindo
                self.rect.top = block.rect.bottom
                self.speedy = 0

        if pygame.sprite.spritecollide(self, self.spikes, False):
            self.morto = True
            
        

        self.isJump = not on_ground  # ATUALIZA AQUI

        # Limites da tela
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > self.HEIGHT:
            self.rect.bottom = self.HEIGHT
            self.speedy = 0
            self.isJump = False

    def jump(self):
        if not self.isJump:
            self.speedy = self.jump_force
            self.isJump = True
