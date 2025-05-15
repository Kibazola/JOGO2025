import pygame

class Pessoa(pygame.sprite.Sprite):
    def _init_(self, img_personagem, WIDTH, HEIGHT, blocks):
        super()._init_()
        self.WIDTH = WIDTH     
        self.blocks = blocks
        self.HEIGHT = HEIGHT 
        self.original_image = img_personagem
        self.image = img_personagem
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-15, -20)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        

        self.speedx = 0
        self.speedy = 0
        self.jump_force = -15
        self.gravity = 1
        self.isJump = False
        self.blocks = blocks
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.facing_right = True  # NOVO: direção inicial

    def update(self):
        # Atualiza direção
        if self.speedx > 0:
            self.facing_right = True
        elif self.speedx < 0:
            self.facing_right = False

        # Aplica direção à imagem
        if self.facing_right:
            self.image = pygame.transform.flip(self.original_image, True, False)
        else:
            self.image = self.original_image

        # Movimento horizontal
        self.rect.x += self.speedx

        # Colisão horizontal
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in collisions:
            if self.speedx > 0:
                self.rect.right = block.rect.left
            elif self.speedx < 0:
                self.rect.left = block.rect.right

        # Gravidade
        self.speedy += self.gravity
        self.rect.y += self.speedy

        # Colisão vertical
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        if collisions:
            for block in collisions:
                if self.speedy > 0:
                    self.rect.bottom = block.rect.top
                    self.isJump = False
                elif self.speedy < 0:
                    self.rect.top = block.rect.bottom
                self.speedy = 0
        else:
            self.isJump = True

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