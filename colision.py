import pygame
import enemigo

colisiones = pygame.sprite.spritecollide(jugador, mons, False)
for enemigo in colisiones:
    enemigo.image = pygame.image.load("Recursos juego/explosión.png")
    enemigo.rect.y += 10  # Hace que el enemigo caiga hacia abajo
    if enemigo.rect.top > 670:
        enemigo.kill()
