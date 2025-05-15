
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

# Classe do bloco como sprite
class Bloco(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Classe World (mundo do jogo)
class World():
    def __init__(self, data):
        self.bloco_group = pygame.sprite.Group()

        # carrega imagens
        dirt_img = pygame.image.load('assets/img/dirt.png')
        grass_img = pygame.image.load('assets/img/grass.png')
        spike_img = pygame.image.load('assets/img/Short_Spike_Row.webp')

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
                    self.bloco_group.add(bloco)

                col_count += 1
            row_count += 1

    def draw(self, screen):
        self.bloco_group.draw(screen)


