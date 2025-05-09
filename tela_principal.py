import pygame
from tela_de_carregamento import tela_carregamento
import random
pygame.init()
pygame.mixer.init()

WIDTH = 1600
HEIGHT = 870
p_WIDTH = 100
p_HEIGHT = 200
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Kiba!')
#Criando as imagens
background = pygame.image.load('assets/img/fundo novo.jpg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
img_personagem = pygame.image.load('assets/img/personagem_normal-removebg-preview (1).png').convert_alpha()
img_personagem = pygame.transform.scale(img_personagem, (p_WIDTH, p_HEIGHT))
img_morcego = [pygame.image.load('assets/img/voando/0-removebg-preview.png'),
               pygame.image.load('assets/img/voando/1-removebg-preview.png'),
               pygame.image.load('assets/img/voando/2-removebg-preview.png'),
               pygame.image.load('assets/img/voando/4-removebg-preview.png'),
               pygame.image.load('assets/img/voando/5-removebg-preview.png')
               ]
# Chama a função importada de tela de carregamento
tela_carregamento(window, WIDTH, HEIGHT)

music = pygame.mixer.Sound('assets/snd/Cinematic Drums Epic Percussion Background Music by Alec Koff.mp3')
music.set_volume(0.5)  #  ajusta o volume
music.play(loops=-1)
morcego_posição_de_começo = (100,250)

#Criando a classe Morcego:
#Esta classe foi bassenado no seguinte tutorial: 
#https://www.youtube.com/watch?v=RERGFvpRWVA
class Morcego(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = img_morcego[0]
        self.rect = self.image.get_rect()
        self.rect.center = morcego_posição_de_começo
        self.image_index = 0
        self.speedx = random.randint(3, 7)  # velocidade aleatória

    def reset_pos(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, 200)

    def update(self):
        #Animação do morcego
        self.image_index +=1
        if  self.image_index >=30:
            self.image_index = 0
        self.image = img_morcego[self.image_index // 10]

        self.rect.x += self.speedx

        # Se sair da tela, reposiciona no topo com nova velocidade
        if self.rect.left > WIDTH:
            self.reset_pos()
            self.speedx = random.randint(3, 7)
       





#Criando a classe pessoa:
class Pesssoa(pygame.sprite.Sprite):
    def __init__(self,img_personagem ):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img_personagem
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.isJump = False
        self.jumpCount = 15
        self.jumpSpeed = 8 

    def update(self):
        if not self.isJump:
            self.rect.x += self.speedx
        else:
            # movimento horizontal no ar
            if self.speedx != 0:
                self.rect.x += self.jumpSpeed if self.speedx > 0 else -self.jumpSpeed

            # movimento vertical em forma de arco
            if self.jumpCount >= -10:
                neg = 1 if self.jumpCount > 0 else -1
                self.rect.y -= (self.jumpCount ** 2) * 0.3 * neg
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False

        # Limites da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        # Imagem virada para a direita/esquerda
        if self.speedx < 0:
            self.image = img_personagem
        elif self.speedx > 0:
            self.image = pygame.transform.flip(img_personagem, True, False)


# Loop principal do jogo
game = True

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30


# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
# Criando o jogador
player =Pesssoa(img_personagem)
all_sprites.add(player)

#Criando o Morcego
morcego1= pygame.sprite.GroupSingle()
morcego2= pygame.sprite.GroupSingle()
morcego1.add(Morcego())
morcego2.add(Morcego())

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            game = False
        #Os códigos para poder pular foram baseados no seguinte tutorial: https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping
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

    #window.fill((0,0,0))
    window.blit(background, (0,0))
    #pygame.display.update()
    #Desenhando a pessoa na tela
    all_sprites.draw(window)
    morcego1.draw(window)
    morcego2.draw(window)


    #Atualize a tela depois de desenhar
    pygame.display.update()

pygame.quit()