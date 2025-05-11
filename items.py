import pygame
pygame.init()
WIDTH = 1600
HEIGHT = 870
window = pygame.display.set_mode((WIDTH, HEIGHT))

# esta classe foi baseado no seguinte tutorial:
TILE_SIZE = 64

img_vida =  pygame.image.load('assets/img/items/vida-removebg-preview.png').convert_alpha()
img_vida= pygame.transform.scale(img_vida, (100, 100))
img_espinho = pygame.image.load('assets/img/items/espinho-removebg-preview.png').convert_alpha()
img_espinho= pygame.transform.scale(img_espinho, (150,200 ))
img_moeda = pygame.image.load('assets/img/items/moeda-removebg-preview.png').convert_alpha()
img_moeda= pygame.transform.scale(img_moeda, (100, 100))

item_boxes = {
    "vida"    : img_vida,
    "espinho" : img_espinho,
    "moeda"   : img_moeda
}


class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-60, -60)
        self.rect.midtop = (x + TILE_SIZE//2, y + (TILE_SIZE - self.image.get_height()))