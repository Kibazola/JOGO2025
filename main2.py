import pygame
from tela_de_carregamento import tela_carregamento
from pessoa import*
from morcego import Morcego
import random
from items import ItemBox
from time import sleep
from plataforma2 import*
from tela_de_carregamento2 import*



pygame.init()
pygame.mixer.init()


WIDTH = 1600
HEIGHT = 900
p_WIDTH = 75
p_HEIGHT = 130
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo')

# Criando as imagens
winner_img = pygame.image.load('assets/img/istockphoto.jpg').convert()
winner_img = pygame.transform.scale(winner_img, (WIDTH, HEIGHT))
game_over_img = pygame.image.load('assets/img/game_over1.webp').convert()
game_over_img = pygame.transform.scale(game_over_img, (WIDTH, HEIGHT))
background = pygame.image.load('assets/img/main2/IMG-20250517-WA0004.jpg').convert()
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




# Chama a função tela de carregamento2:
tela_carregamento2(window, WIDTH, HEIGHT)


music_dor =  pygame.mixer.Sound('assets/snd/som_dor.wav')
gm_music = pygame.mixer.Sound('assets/snd/GAME OVER efeito sonoro!!.mp3')
moeda_musc = pygame.mixer.Sound('assets/snd/MOEDA DO SUPER MÁRIO.mp3')

music_morcego = pygame.mixer.Sound('assets/snd/SOM DE MORCEGOSSOUND OF BAT.mp3')
music_morcego.set_volume(0.05)
music_jump = pygame.mixer.Sound('assets/snd/mixkit-player-jumping-in-a-video-game-2043.wav')


font_pontuação = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

# Loop principal do jogo
game = True

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de sprites
all_sprites = pygame.sprite.Group()
all_morcegos = pygame.sprite.Group()
porta_sprit = pygame.sprite.Group()
moedas = pygame.sprite.Group()
blocos = pygame.sprite.Group()


#Criando matriz de plataforma do jogo (nivel2)
world_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,4,0,4,0,0,0,4,0,0,0,4,0,4,4,0,0,0,0,1],
    [1,2,0,6,0,0,0,6,0,0,0,2,0,6,6,0,0,0,4,1],
    [1,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,4,2,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,2,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,6,0,0,0,1,1,0,0,1],
    [1,0,0,0,0,4,4,4,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,2,2,2,0,5,0,0,0,0,0,0,0,0,0,1],
    [1,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1],
]

# Criação do mundo
world = World(world_data)


start_x = 1000
start_y = 500 


player_sprites = { 
    "idle": "assets/img/Personagem/parado.png",
    "run1": "assets/img/Personagem/mov1.png",
    "run2": "assets/img/Personagem/mov2.png",
    "jump": "assets/img/Personagem/mov2.png"
}
player = Pessoa(player_sprites, start_x, start_y,world.moeda_group,world.bloco_group, world.spike_group,WIDTH, HEIGHT)
all_sprites.add(player)


#Criando os morcegos:
for i in range(3):
    morcego = Morcego(img_morcego[i], WIDTH)
    all_sprites.add(morcego)
    all_morcegos.add(morcego)

#Criando o item porta:
porta = ItemBox("porta",55, 197)
all_sprites.add(porta)
porta_sprit.add(porta)

pontos = 0
lives = 4
colidindo = False




cont_m = False
while game:

    clock.tick(FPS)
    world.update()
    #O bloco abaixo foi gerado por AI (ChatGPT)
    #Faz com o jogador se mova com a velocidade do bloco, quando ele estiver parado sobre o bloco
    for bloco in world.bloco_group:
        if hasattr(bloco, 'speedx'):  # Verifica se o bloco se move
            if player.rect.bottom <= bloco.rect.top + 5 and \
            player.rect.bottom >= bloco.rect.top - 5 and \
            player.rect.centerx >= bloco.rect.left and \
            player.rect.centerx <= bloco.rect.right:
                player.rect.x += bloco.speedx

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            game = False

        # Os códigos para pular foram baseados no tutorial:
        # https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping
        if lives > 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx = -8 
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                if event.key == pygame.K_SPACE and not player.isJump:
                    player.jump()
                    music_jump.play()
        else:
            window.blit(game_over_img, (10, 10))
            pygame.display.update()
            music_morcego.stop()
            #music.stop()
            sleep(1)
            if not cont_m:
                cont_m = True
                gm_music.play()
                pygame.display.update()
                continue  # Pula o resto do loop se o jogo acabou
            
            if event.key == pygame.K_SPACE:
                    # Reinicia o jogo
                    lives = 4
                    pontos = 0
                    colidindo = False
                    #music.play()
                    # Remove todos os obstáculos
                    for obstaculo in all_morcegos:
                        if obstaculo != player:  # Não remove o jogador
                            obstaculo.kill()

                    #Criando os morcegos:
                    for i in range(3):
                        morcego = Morcego(img_morcego[i], WIDTH)
                        all_sprites.add(morcego)
                        all_morcegos.add(morcego)

                    
                    # Reposiciona o jogador
                    player.rect.x = 1000
                    player.rect.y = 500
                    player.isJump = False
                    player.speedx = 0
                    player.morto = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                        player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8


    # ----- Atualiza estado do jogo
    # Atualizando a posição dos morcegos

    if lives > 0:
        all_sprites.update()
    else:
        # Mostra tela de game over
       # window.blit(background, (0, 0))
        window.blit(game_over_img, (10, 10))
        pygame.display.update()
        music_morcego.stop()
       # music.stop()
        sleep(2)
        if not cont_m:
            cont_m = True
            gm_music.play()
        pygame.display.update()
        continue  # Pula o resto do loop se o jogo acabou

    #Este bloco trata o que acontece quando o jogador morre no jogo. De forma geral:
    if player.morto:
        music_dor.play()
        lives -= 2
        player.rect.x = 1000
        player.rect.y = 500
        player.isJump = False
        player.speedx = 0
        player.morto = False
        all_sprites.update()

    #Este bloco trata o que acontece quando o colide com os morcegos:
    hits = pygame.sprite.spritecollide(player,all_morcegos, False)
    if hits:
        if hits and not colidindo:

            music_dor.play()
            lives -=1
            colidindo = True
            cont_m = False
    else:
        colidindo = False
        

    #Verifica se houve colisão entre o jogador  e moeda   
    if player.recolhida:
        pontos+=25
        moeda_musc.play()
        if pontos % 1000 ==0:
            lives+=1
        player.recolhida = False


    #Verifica se houve colisão entre o jogador e a porta
    hits_porta = pygame.sprite.spritecollide(player, porta_sprit, False)
    if hits_porta:
        music_morcego.stop()
        window.blit(winner_img, (10, 10))
        pygame.display.update()
        sleep(15)
        
        
    
    #---- Gera saídas
    window.blit(background, (0, 0))
    world.draw(window)
    # Desenhando os morcegos
    all_sprites.draw(window)

    # Desenhando o score
    text_surface = font_pontuação.render("{:08d}".format(pontos), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  15)
    window.blit(text_surface, text_rect)

    # Desenhando as vidas
    text_surface = font_pontuação.render(chr(9829) * lives, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (30, HEIGHT - 30)
    window.blit(text_surface, text_rect)

    pygame.display.update()

pygame.quit()