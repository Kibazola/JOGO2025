import pygame
from tela_de_carregamento import tela_carregamento
from pessoa import Pessoa
from morcego import Morcego
import random


pygame.init()
pygame.mixer.init()

WIDTH = 1600
HEIGHT = 870
p_WIDTH = 100
p_HEIGHT = 200
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Kiba!')

# Criando as imagens
background = pygame.image.load('assets/img/fundo novo.jpg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
img_personagem = pygame.image.load('assets/img/personagem_normal-removebg-preview (1).png').convert_alpha()
img_personagem = pygame.transform.scale(img_personagem, (p_WIDTH, p_HEIGHT))

# Chama a função tela de carregamento:
tela_carregamento(window, WIDTH, HEIGHT)

music = pygame.mixer.Sound('assets/snd/Cinematic Drums Epic Percussion Background Music by Alec Koff.mp3')
music.set_volume(0.5)  # ajusta o volume
music.play(loops=-1)



# Loop principal do jogo
game = True

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de sprites
all_sprites = pygame.sprite.Group()

# Criando o jogador
player = Pessoa(img_personagem, WIDTH, HEIGHT)
all_sprites.add(player)



morcego1 = pygame.sprite.GroupSingle()
morcego2 = pygame.sprite.GroupSingle()
morcego3 = pygame.sprite.GroupSingle()
morcego1.add(Morcego(WIDTH))
morcego2.add(Morcego(WIDTH))
morcego3.add(Morcego(WIDTH))


while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            game = False
        # Os códigos para pular foram baseados no tutorial:
        # https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx = -8
            if event.key == pygame.K_RIGHT:
                player.speedx = 8
            if event.key == pygame.K_SPACE and not player.isJump:
                player.isJump = True

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.speedx = 0

    all_sprites.update()
    morcego1.update()
    morcego2.update()
    morcego3.update()

    window.blit(background, (0, 0))
    all_sprites.draw(window)
    morcego1.draw(window)
    morcego2.draw(window)
    morcego3.draw(window)
    
     



    pygame.display.update()

pygame.quit()