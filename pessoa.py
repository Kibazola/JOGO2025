import pygame

class Pessoa(pygame.sprite.Sprite):
    def __init__(self, img_paths, start_x, start_y, moeda, blocks, spikes, screen_width, screen_height):
        super().__init__()
        
        # Carrega os frames de animação
        # O bloco de código abaixo foi gerado por AI (ChatGPT)
        self.frames = {
            'idle': [pygame.image.load("assets/img/Personagem/parado.png").convert_alpha()],
            'run': [pygame.image.load(f"assets/img/Personagem/mov{i}.png").convert_alpha() for i in range(1, 3)],
            'jump': [pygame.image.load("assets/img/Personagem/mov2.png").convert_alpha()]
        }
        
        # Redimensiona os frames (ajuste conforme necessário)
        for action in self.frames:
            for i, frame in enumerate(self.frames[action]):
                self.frames[action][i] = pygame.transform.scale(frame, (75, 130))
        
        self.current_frame = 0
        self.animation_speed = 0.25
        self.state = 'idle'
        self.image = self.frames[self.state][0]
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-20, -20)

        # Configurações de movimento (mantidas do seu código original)
        self.speedx = 0
        self.speedy = 0
        self.jump_force = -15
        self.gravity = 1
        self.isJump = False
        self.blocks = blocks
        self.moeda = moeda
        self.WIDTH = screen_width
        self.HEIGHT = screen_height
        self.spikes = spikes

        self.facing_right = True
        self.morto = False
        self.recolhida = False
        self.rect.x = start_x
        self.rect.y = start_y

    def animate(self):
        # Atualiza o frame atual
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.frames[self.state]):
            self.current_frame = 0
        
        # Seleciona o frame e aplica a direção
        frame = self.frames[self.state][int(self.current_frame)]

        # Aplica flip apenas se estiver virado para a esquerda
        if not self.facing_right:
            frame = pygame.transform.flip(frame, True, False)  # Inverte horizontalmente

        self.image = frame

    def update(self):
        # Atualiza a direção (VERIFICA SE HÁ MOVIMENTO)
        if self.speedx > 0:  # Direita
            self.facing_right = True
        elif self.speedx < 0:  # Esquerda
            self.facing_right = False
        
        # Define o estado com base no movimento
        if self.isJump:
            self.state = "jump"
        elif self.speedx != 0:
            self.state = 'run'
        else:
            self.state = 'idle'

        # Atualiza animação
        self.animate()


        # Movimento vertical (código original)
        self.speedy += self.gravity
        self.rect.y += self.speedy
        on_ground = False

        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in collisions:
            if self.speedy > 0:
                self.rect.bottom = block.rect.top
                self.speedy = 0
                on_ground = True
            elif self.speedy < 0:
                self.rect.top = block.rect.bottom
                self.speedy = 0

        # Movimento horizontal (código original)
        self.rect.x += self.speedx
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in collisions:
            if self.speedx > 0:
                self.rect.right = block.rect.left
            elif self.speedx < 0:
                self.rect.left = block.rect.right

        # Colisões (código original)
        if pygame.sprite.spritecollide(self, self.spikes, False):
            self.morto = True
        if pygame.sprite.spritecollide(self, self.moeda, True):
            self.recolhida = True

        self.isJump = not on_ground

        # Limites da tela (código original)
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > self.HEIGHT:
            self.rect.bottom = self.HEIGHT
            self.speedy = 0
            self.isJump = False

    def jump(self):
        if not self.isJump:
            self.speedy = self.jump_force
            self.isJump = True