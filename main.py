import pygame
import random
import time
from pygame.locals import *

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
 # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
    # Rectángulo (jugador)
        self.image = pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_1.png").convert()
    # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
    # Centra el rectángulo (sprite)
        self.rect.center = (0, 370)
        self.velocidad_x = 0


    def update(self):
        self.velocidad_x = 0

    # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()
    # Mueve al personaje hacia la izquierda
        if teclas[pygame.K_a]:
           self.velocidad_x = -5
        if teclas[pygame.K_d]:
           self.velocidad_x = 5
    # Actualiza la velocidad del personaje.
        self.rect.x += self.velocidad_x


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Recursos juego/SPRITES/MOUNSTROS/FUEGO/fueguitox_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (850 // 1, 535 // 1)

        self.velocidad_x = 2
        self.velocidad_y = 2

    def update(self):
        self.rect.x -= self.velocidad_x
        #self.rect.y += self.velocidad_y
        # Limita el margen derecho
        if self.rect.right > 850:
            self.rect.right = 850

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.rect.left = 0

        # Limita el margen inferior
        if self.rect.bottom > 470:
            self.rect.bottom = 470

        # Limita el margen superior
        if self.rect.top < 0:
            self.rect.top = 0


pygame.init()
PANTALLA = pygame.display.set_mode((850, 670))
pygame.display.set_caption('No dormí ayuda')
clock = pygame.time.Clock()
icono = pygame.image.load("Recursos juego/SPRITES/MOUNSTROS/FUEGO/fueguitox_1.png")
pygame.display.set_icon(icono)

spawn_interval = 5  # Intervalo de tiempo entre apariciones (en segundos)
total_time = 60
spawn_count = total_time // spawn_interval  # Cantidad de veces que el bucle debe iterar

sprites = pygame.sprite.Group()
mons = pygame.sprite.Group()

juga= Jugador()
sprites.add(juga)

for _ in range(spawn_count):
    enemigo= Enemigo()
    mons.add(enemigo)

    start_time = time.time()


ejecutando = True
while ejecutando:
    clock.tick(60)  # Limitar el juego a 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    sprites.update()
    mons.update()
    for monster in mons:
        PANTALLA.blit(monster.image, monster.rect)
    pygame.display.flip()
    clock.tick(60)


    PANTALLA.fill(BLANCO)  # Limpia la pantalla con color blanco

    sprites.draw(PANTALLA)  # Dibuja los sprites en la pantalla
    mons.draw(PANTALLA)
    pygame.display.flip()
    elapsed_time = time.time() - start_time  # Tiempo transcurrido desde el inicio del juego

    if elapsed_time >= total_time:
        running = False
pygame.quit()
