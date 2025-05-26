import pygame
from pygame.locals import *
pygame.init()

WIDTH = 1600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platformer')

# load images
tile_size = 80

background = pygame.image.load('assets/img/fundo novo.jpg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
# A construção deste arquivo de plataforma foi passeada no seguinte GitHub:
#https://github.com/Insper/pygame-snippets/blob/master/jump_block.py

# Classe do bloco como sprite
class Bloco(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Bloco_movel(pygame.sprite.Sprite):
    def __init__(self,img, x,y,m_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speedy = -8
        self.min_y =  m_y
        self.max_y = y 




#



    def update(self):
        self.rect.y += self.speedy
        if self.rect.y < self.min_y and self.speedy  <0:
            self.speedy = - self.speedy 
            self.rect.y = self.min_y


        if self.rect.y > self.max_y and self.speedy  >0:
            self.speedy = - self.speedy 
            self.rect.y = self.max_y



    ######

class Bloco_movel_x(pygame.sprite.Sprite):
    def __init__(self, img, x, y, distancia_x=15):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speedx = 2  # velocidade no eixo x

        # min_x e max_x baseados na mesma distância a partir da posição inicial
        self.min_x = x 
        self.max_x = x + distancia_x // 2

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x < self.min_x and self.speedx < 0:
            self.speedx = -self.speedx
            self.rect.x = self.min_x
        if self.rect.x > self.max_x and self.speedx > 0:
            self.speedx = -self.speedx
            self.rect.x = self.max_x

# Classe World (mundo do jogo)
class World():
    def __init__(self, data):
        self.bloco_group = pygame.sprite.Group()
        self.spike_group = pygame.sprite.Group()
        self.moeda_group = pygame.sprite.Group()

        # carrega imagens
        dirt_img = pygame.image.load('assets/img/main2/normal.jpg')
        grass_img = pygame.image.load('assets/img/main2/plat.jpg')
        spike_img = pygame.image.load('assets/img/Short_Spike_Row.webp')
        moeda_img = pygame.image.load('assets/img/items/moeda-removebg-preview.png').convert_alpha()

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                x = col_count * tile_size
                y = row_count * tile_size

                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    bloco = Bloco(img, x, y)
                    self.bloco_group.add(bloco)

                elif tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    bloco = Bloco(img, x, y)
                    self.bloco_group.add(bloco)

                elif tile == 3:
                    img = pygame.transform.scale(spike_img, (tile_size, tile_size))
                    bloco = Bloco(img, x, y)
                    self.spike_group.add(bloco)
                
                elif tile == 4:
                    img = pygame.transform.scale(moeda_img, (tile_size, tile_size))
                    moeda = Bloco(img, x, y)
                    self.moeda_group.add(moeda)

                elif tile == 5:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    bloco = Bloco_movel(img, x, y,5*tile_size)
                    self.bloco_group.add(bloco)

                elif tile == 6:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    bloco = Bloco_movel_x(img, x, y,2*tile_size)
                    self.bloco_group.add(bloco)


                col_count += 1
            row_count += 1

    def draw(self, screen):
        self.bloco_group.draw(screen)
        self.spike_group.draw(screen)
        self.moeda_group.draw(screen)


    def update(self):
       
       self.bloco_group.update()


