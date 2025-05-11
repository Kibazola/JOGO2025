import pygame
from tela_de_carregamento import tela_carregamento
from pessoa import Pessoa
from morcego import Morcego
import random
from items import ItemBox
from time import sleep


pygame.init()
pygame.mixer.init()

WIDTH = 1600
HEIGHT = 870
p_WIDTH = 100
p_HEIGHT = 200
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo')

# Criando as imagens
background = pygame.image.load('assets/img/fundo novo.jpg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
img_personagem = pygame.image.load('assets/img/personagem_normal-removebg-preview (1).png').convert_alpha()
img_personagem = pygame.transform.scale(img_personagem, (p_WIDTH, p_HEIGHT))

p_WIDTH = 100
p_HEIGHT = 100

img_morcego = [
    pygame.transform.scale(pygame.image.load('assets/img/voando/0-removebg-preview.png'), (p_WIDTH, p_HEIGHT)),
    pygame.transform.scale(pygame.image.load('assets/img/voando/1-removebg-preview.png'), (p_WIDTH, p_HEIGHT)),
    pygame.transform.scale(pygame.image.load('assets/img/voando/2-removebg-preview.png'), (p_WIDTH, p_HEIGHT)),
    pygame.transform.scale(pygame.image.load('assets/img/voando/4-removebg-preview.png'), (p_WIDTH, p_HEIGHT)),
    pygame.transform.scale(pygame.image.load('assets/img/voando/5-removebg-preview.png'), (p_WIDTH, p_HEIGHT))
]



# Chama a função tela de carregamento:
tela_carregamento(window, WIDTH, HEIGHT)

music = pygame.mixer.Sound('assets/snd/Cinematic Drums Epic Percussion Background Music by Alec Koff.mp3')
music.set_volume(0.5)  # ajusta o volume
music.play(loops=-1)
music_dor =  pygame.mixer.Sound('assets/snd/som_dor.wav')
font_pontuação = pygame.font.Font('assets/font/PressStart2P.ttf', 28)



# Loop principal do jogo
game = True

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de sprites
all_sprites = pygame.sprite.Group()
all_morcegos_e_espinhos = pygame.sprite.Group()
all_moedas = pygame.sprite.Group()


# Criando o jogador
player = Pessoa(img_personagem, WIDTH, HEIGHT)
all_sprites.add(player)

#Criando os morcegos:
for i in range(3):
    morcego = Morcego(img_morcego[i], WIDTH)
    all_sprites.add(morcego)
    all_morcegos_e_espinhos.add(morcego)

#Criando o items espinhos:
# Este código foi gerado por AI
for i in range(2):  # quantidade de espinhos
    x = random.randint(200, WIDTH - 200)
    x_m = random.randint(200, WIDTH - 200)
    y = random.randint(300, 800)
    # Evita que a moeda fique muito perto do espinho
    while abs(x - x_m) < 100:
        x_m = random.randint(200, WIDTH - 200)
    espinho = ItemBox("espinho", x, 800)
    moeda = ItemBox("moeda", x_m, 800)
   

    all_sprites.add(espinho)
    all_sprites.add(moeda)
    all_morcegos_e_espinhos.add(espinho)
    all_moedas.add(moeda)


pontos = 0
lives = 3
colidindo = False




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
            if event.key == pygame.K_LEFT:
                        player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8


    # ----- Atualiza estado do jogo
    # Atualizando a posição dos morcegos

    all_sprites.update()


    # Verifica se houve colisão entre o jogador e morcego ou espinho

    if lives ==0:
        music_dor.play()
        sleep(2)
        game = False
    hits = pygame.sprite.spritecollide(player,all_morcegos_e_espinhos, False)

    if hits:
        if hits and not colidindo:

            music_dor.play()
            lives -=1
            colidindo = True
    else:
        colidindo = False
        

    #Verifica se houve colisão entre o jogador  e moeda
    hits_m = pygame.sprite.spritecollide(player,all_moedas, False)
    if hits_m:
        pontos+=25
        if pontos % 1000 ==0:
            lives+=1
        for moeda in hits_m:

        # reposiciona a moeda em nova posição no chão
            nova_x = random.randint(200, WIDTH - 200)
            moeda.rect.x = nova_x

    
        
    

    #---- Gera saídas
    window.blit(background, (0, 0))
    # Desenhando os morcegos
    all_sprites.draw(window)

    # Desenhando o score
    text_surface = font_pontuação.render("{:08d}".format(pontos), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    # Desenhando as vidas
    text_surface = font_pontuação.render(chr(9829) * lives, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (10, HEIGHT - 10)
    window.blit(text_surface, text_rect)

    pygame.display.update()

pygame.quit()