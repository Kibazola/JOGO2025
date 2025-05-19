import pygame
import time

def tela_carregamento2(window, WIDTH, HEIGHT):
    font = pygame.font.SysFont(None, 60)
    img_fundo = pygame.image.load('assets/img/main/fundomain.png').convert()
    img_fundo = pygame.transform.scale(img_fundo, (WIDTH, HEIGHT))
    

    
    progresso = 0

    
    while progresso <= 100:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        window.fill((0, 0, 0))
        window.blit(img_fundo, (10, 10))
        pygame.draw.rect(window, (255, 255, 255), (500, 700, 600, 40), 3)
        pygame.draw.rect(window, (50, 255, 50), (503, 703, 6 * progresso - 6, 34))

        texto = font.render(f"Carregando... {progresso}%", True, (255, 255, 255))
        window.blit(texto, (WIDTH // 2 - texto.get_width() // 2, 750))

        pygame.display.update()
        pygame.time.delay(300)
        progresso += 2


    tela_carregamento2(window, WIDTH, HEIGHT)

    