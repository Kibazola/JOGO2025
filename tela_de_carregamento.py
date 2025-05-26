#Este 
import pygame
import time

def tela_carregamento(window, WIDTH, HEIGHT):
    font = pygame.font.SysFont(None, 60)
    img_fundo = pygame.image.load('assets/img/imagemcapa.png').convert()
    img_fundo = pygame.transform.scale(img_fundo, (WIDTH, HEIGHT))
    music_inicio = pygame.mixer.Sound('assets/snd/William Rosati - Floating Also ♫ NO COPYRIGHT 8-bit Music.mp3')

    music_inicio.play()

   
    # Este bloco de código abaixo foi 80% gerada por AI (ChatGPT)
    #Descrição do código abaixo:
    #Este código implementa uma tela de carregamento visual usando a biblioteca Pygame.
    #Ele exibe uma barra de progresso que vai de 0% a 100%, acompanhada de um texto indicando o andamento do carregamento. 
    #Durante esse processo, a tela é atualizada continuamente com uma imagem de fundo, o contorno da barra e o preenchimento proporcional ao progresso


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

    music_inicio.stop()
