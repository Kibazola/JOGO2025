import pygame

# Criando a classe Pessoa:
class Pessoa(pygame.sprite.Sprite):
    def __init__(self, img_personagem, WIDTH, HEIGHT):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.original_image = img_personagem
        self.image = img_personagem
        self.rect = self.image.get_rect()
        
        self.rect = self.rect.inflate(-60, -20)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.isJump = False
        self.jumpCount = 15
        self.jumpSpeed = 8 
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def update(self):
        if not self.isJump:
            self.rect.x += self.speedx
        else:
            # movimento horizontal no ar
            if self.speedx != 0:
                self.rect.x += self.jumpSpeed if self.speedx > 0 else -self.jumpSpeed

            # movimento vertical em forma de arco
            if self.jumpCount >= -15:
                neg = 1 if self.jumpCount > 0 else -1
                self.rect.y -= (self.jumpCount ** 2) * 0.3 * neg
                self.jumpCount -= 1
            else:
                self.jumpCount = 15
                self.isJump = False

        # Limites da tela
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > self.HEIGHT:
            self.rect.bottom = self.HEIGHT

        # Imagem virada para a direita/esquerda
        if self.speedx < 0:
            self.image = self.original_image
        elif self.speedx > 0:
            self.image = pygame.transform.flip(self.original_image, True, False)