import pygame
import random
pygame.mixer.init()
# Criando as imagens dos morcegos
p_WIDTH = 100
p_HEIGHT = 100

img_morcego = [
    pygame.transform.scale(pygame.image.load('assets/img/voando/0-removebg-preview.png'), (p_WIDTH, p_HEIGHT)),
    pygame.transform.scale(pygame.image.load('assets/img/voando/1-removebg-preview.png'), (p_WIDTH, p_HEIGHT)),
    pygame.transform.scale(pygame.image.load('assets/img/voando/2-removebg-preview.png'), (p_WIDTH, p_HEIGHT)),
    pygame.transform.scale(pygame.image.load('assets/img/voando/4-removebg-preview.png'), (p_WIDTH, p_HEIGHT)),
    pygame.transform.scale(pygame.image.load('assets/img/voando/5-removebg-preview.png'), (p_WIDTH, p_HEIGHT))
]

music_morcego = pygame.mixer.Sound('assets/snd/SOM DE MORCEGOSSOUND OF BAT.mp3')

music_morcego.set_volume(0.05)

# Criando a classe Morcego:
# Esta classe foi baseada no seguinte tutorial: 
# https://www.youtube.com/watch?v=RERGFvpRWVA
class Morcego(pygame.sprite.Sprite):
    def __init__(self,img_morcego, WIDTH):
        pygame.sprite.Sprite.__init__(self)
        self.image = img_morcego
        self.rect = self.image.get_rect()
        self.rect.center = (0, 500)
        self.image_index = 0
        self.speedx = random.randint(0, 7)
        self.WIDTH = WIDTH
        music_morcego.play()

    def reset_pos(self):
        self.rect.x = random.randint(0, self.WIDTH - self.rect.width)
        self.rect.y = random.randint(0, 200)
        music_morcego.play()

    def update(self):
        # Animação do morcego
        self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = img_morcego[self.image_index // 10]

        self.rect.x += self.speedx

        # Se sair da tela, reposiciona no topo com nova velocidade
        if self.rect.left > self.WIDTH:
            self.reset_pos()
            self.speedx = random.randint(3, 10)