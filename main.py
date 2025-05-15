
import pygame
from tela_de_carregamento import tela_carregamento
from pessoa import*
from morcego import Morcego
import random
from items import ItemBox
from time import sleep
from plataforma import*


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
gm_music = pygame.mixer.Sound('assets/snd/GAME OVER efeito sonoro!!.mp3')
moeda_musc = pygame.mixer.Sound('assets/snd/MOEDA DO SUPER MÁRIO.mp3')
winner_music = pygame.mixer.Sound('assets/snd/Rocket Jr - A Lil BIT _ Eccentric, Quirky _ Bit Music-yt.savetube.me.mp3')
music_morcego = pygame.mixer.Sound('assets/snd/SOM DE MORCEGOSSOUND OF BAT.mp3')
music_morcego.set_volume(0.05)
music_jump = pygame.mixer.Sound('assets/snd/mixkit-player-jumping-in-a-video-game-2043.wav')
# Loop principal do jogo
game = True

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de sprites
all_sprites = pygame.sprite.Group()
all_morcegos = pygame.sprite.Group()
all_moedas = pygame.sprite.Group()
porta_sprit = pygame.sprite.Group()

blocos = pygame.sprite.Group()

world_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,2,2,0,2,3,2,2,0,2,0,2,0,2,1],
    [1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,2,2,0,0,0,0,2,2,2,2,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,1],
]

# Criação do mundo
world = World(world_data)

# Criando o jogador
# player = Pessoa(img_personagem, WIDTH, HEIGHT, world.bloco_group,world.spike_group)
# all_sprites.add(player)
start_x = 1000
start_y = 500 #HEIGHT - tile_size * 2
player = Pessoa(img_personagem, start_x, start_y, world.bloco_group, world.spike_group,WIDTH, HEIGHT)
all_sprites.add(player)


#Criando os morcegos:
for i in range(3):
    morcego = Morcego(img_morcego[i], WIDTH)
    all_sprites.add(morcego)
    all_morcegos.add(morcego)

#Criando o items espinhos:
# Este código foi gerado por AI

for i in range(2):  # quantidade de espinhos
    x = random.randint(200, WIDTH - 200)
    x_m = random.randint(200, WIDTH - 200)
    y = random.randint(300, 800)
    # Evita que a moeda fique muito perto do espinho
    while abs(x - x_m) < 100:
        x_m = random.randint(200, WIDTH - 200)
    moeda = ItemBox("moeda", x_m, 750)


    all_sprites.add(moeda)
    all_moedas.add(moeda)


porta = ItemBox("porta",1423, 223)
all_sprites.add(porta)
porta_sprit.add(porta)
pontos = 0
lives = 3
colidindo = False




cont_m = False
while game:

    clock.tick(FPS)

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
                    #tplayer.isJump = True
                    music_jump.play()
        else:
            if event.key == pygame.K_SPACE:
                    # Reinicia o jogo
                    lives = 3
                    pontos = 0
                    colidindo = False

                    # Remove todos os obstáculos
                    for obstaculo in all_morcegos:
                        if obstaculo != player:  # Não remove o jogador
                            obstaculo.kill()
                    for moeda in all_moedas:
                        if moeda != player:
                            moeda.kill()
                            #Criando os morcegos:
                    for i in range(3):
                        morcego = Morcego(img_morcego[i], WIDTH)
                        all_sprites.add(morcego)
                        all_morcegos.add(morcego)

                    #Criando o items espinhos:
                    # Este código foi gerado por AI

                    for i in range(2):  # quantidade de espinhos
                        x = random.randint(200, WIDTH - 200)
                        x_m = random.randint(200, WIDTH - 200)
                        y = random.randint(300, 800)
                        # Evita que a moeda fique muito perto do espinho
                        while abs(x - x_m) < 100:
                            x_m = random.randint(200, WIDTH - 200)
                        #espinho = ItemBox("espinho", x, 750)
                        moeda = ItemBox("moeda", x_m, 750)
                    

                        #all_sprites.add(espinho)
                        all_sprites.add(moeda)
                        #all_morcegos_e_espinhos.add(espinho)
                        all_moedas.add(moeda)
                    
                    # Reposiciona o jogador
                    player.rect.x = 50
                    player.rect.y = HEIGHT - 200
                    player.isJump = False
                    player.speedx = 0
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
        sleep(3)
        if not cont_m:
            cont_m = True
            gm_music.play()
        pygame.display.update()
        continue  # Pula o resto do loop se o jogo acabou
    # Verifica se houve colisão entre o jogador e morcego ou espinho


    # Supondo que o nome do seu personagem seja `player`
    if player.morto:
        music_dor.play()
        sleep(1)
        window.blit(game_over_img, (0, 0))  # use (0, 0) para preencher a tela corretamente
        pygame.display.update()
        gm_music.play()
        sleep(5)
        game = False 


    
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
    hits_m = pygame.sprite.spritecollide(player,all_moedas, False)
    if hits_m:
        pontos+=25
        moeda_musc.play()
        if pontos % 1000 ==0:
            lives+=1
        for moeda in hits_m:

        # reposiciona a moeda em nova posição no chão
            nova_x = random.randint(200, WIDTH - 200)
            moeda.rect.x = nova_x

    #Verifica se houve colisão entre o jogador e a porta
    hits_porta = pygame.sprite.spritecollide(player, porta_sprit, False)
    if hits_porta:
        music.stop()
        music_morcego.stop()
        window.blit(winner_img, (10, 10))
        pygame.display.update()
        winner_music.play()
        sleep(15)
        game = False

    
        
    

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