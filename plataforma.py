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

#Esta classe foi baseada no seguinte github:
#https://github.com/russs123/Platformer/blob/master/Part_1-Create_World/platformer_tut1.py
class World():
    def __init__(self, data):
        self.tile_list = []

        # load images
        dirt_img = pygame.image.load('assets/img/dirt.png')
        grass_img = pygame.image.load('assets/img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                col_count += 1
            row_count += 1

    def draw(self,screen ):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])