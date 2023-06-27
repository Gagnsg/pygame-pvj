import pygame
import random
import time
from pygame.locals import *

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Recursos juego/SPRITES/HIT/hit_1.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (100 // 2, 370)
        self.velocidad_x = 0

    def update(self):
        self.velocidad_x = 0
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a]:
            self.velocidad_x = -5
        if teclas[pygame.K_d]:
            self.velocidad_x = 5
        self.rect.x += self.velocidad_x


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Recursos juego/SPRITES/MOUNSTROS/FUEGO/fueguitox_2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (850 // 1, 535 // 1)
        self.velocidad_x = 2
        self.velocidad_y = 2
        self.caida=False
    def update(self):
        if self.caida:
            self.rect.y += 10
            if self.rect.top >670:
                self.kill()
        self.rect.x -= self.velocidad_x
        if self.rect.right > 850:
            self.rect.right = 850
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > 470:
            self.rect.bottom = 470
        if self.rect.top < 0:
            self.rect.top = 0


pygame.init()
PANTALLA = pygame.display.set_mode((850, 670))
pygame.display.set_caption('No dormí ayuda')
clock = pygame.time.Clock()
icono = pygame.image.load("Recursos juego/SPRITES/MOUNSTROS/FUEGO/fueguitox_2.png")
pygame.display.set_icon(icono)

spawn_interval = 5  # Intervalo de tiempo entre apariciones (en segundos)
total_time = 60
spawn_count = total_time // spawn_interval  # Cantidad de veces que el bucle debe iterar

sprites = pygame.sprite.Group()
mons = pygame.sprite.Group()

jugador = Jugador()
sprites.add(jugador)

start_time = time.time()  # Tiempo de inicio del juego
spawn_time = 0

for _ in range(spawn_count):
    enemigo = Enemigo()
    mons.add(enemigo)


ejecutando = True
while ejecutando:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
    elapsed_time = time.time() - start_time
    spawn_time += elapsed_time  # Actualiza el tiempo de aparición acumulativo
    start_time = time.time()  # Reinicia el tiempo de inicio
    if spawn_time >= spawn_interval:
        enemigo = Enemigo()
        mons.add(enemigo)
        spawn_time = 0  # Reinicia el tiempo de aparición acumulativo

    if elapsed_time >= total_time:
        ejecutando = False

    colisiones = pygame.sprite.spritecollide(jugador, mons, False)
    for enemigo in colisiones:
        enemigo.image = pygame.image.load("Recursos juego/explosión.png")
        enemigo.rect.y += 10  # Hace que el enemigo caiga hacia abajo
        enemigo.caida=True
    sprites.update()
    mons.update()

    PANTALLA.fill(BLANCO)
    mons.draw(PANTALLA)
    sprites.draw(PANTALLA)


    pygame.display.flip()

pygame.quit()


