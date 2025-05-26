import pygame
pygame.init()
WIDTH = 1600
HEIGHT = 900
window = pygame.display.set_mode((WIDTH, HEIGHT))


TILE_SIZE = 64

img_vida =  pygame.image.load('assets/img/items/vida-removebg-preview.png').convert_alpha()
img_vida= pygame.transform.scale(img_vida, (100, 100))
img_porta = pygame.image.load('assets/img/items/porta-removebg-preview.png').convert_alpha()
img_porta = pygame.transform.scale(img_porta, (200, 220))

item_boxes = {
    "vida"    : img_vida,
    "porta"   : img_porta
}

#A classe abaixo foi baseado no seguinte tutorial:
class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-60, -60)
        self.rect.midtop = (x + TILE_SIZE//2, y + (TILE_SIZE - self.image.get_height()))







