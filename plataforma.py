import pygame
from pygame.locals import *

pygame.init()

WIDTH = 1600
HEIGHT = 870

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Platformer')

# load images
tile_size = 80
background = pygame.image.load('assets/img/fundo novo.jpg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))