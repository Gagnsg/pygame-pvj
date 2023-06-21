import pygame, sys
from pygame.locals import*
pygame.init()
#Conf. pantalla
WIDTH= 1160
HEIGHT=650
#MEDIDAS CENTRO
cen=WIDTH/2
al=HEIGHT/2
PANTALLA= pygame.display.set_mode((WIDTH, HEIGHT))
#MTítulo, ícono y fondo
pygame.display.set_caption('Jueguito miado')
icon=pygame.image.load("Recursos juego/caca.png")
pygame.display.set_icon(icon)
#FONDO PANTALLA DE INICIO
background_image=pygame.image.load("Recursos juego/fondo.jpg")
background_image=pygame.transform.scale(background_image,(WIDTH,HEIGHT))

#IMAGEN DE TÍTULO
tittle_image=pygame.image.load("Recursos juego/titulo_preview.png")
tittle_image=pygame.transform.scale(tittle_image, (WIDTH,HEIGHT))
tittle_rect= tittle_image.get_rect()
tittle_rect.center= (cen,al)

#CREANDO EL BOTÓN
button_image= pygame.image.load("Recursos juego/inicio-PhotoRoom.png-PhotoRoom.png")
button_image=pygame.transform.scale(button_image, (200,100))
button_rect=button_image.get_rect()
button_rect.center=(cen,al+140)

#SCREEN 2
SCREEN_2= pygame.display.set_mode((WIDTH, HEIGHT))
background_two=pygame.image.load("Recursos juego/fonfodos.png")
background_two=pygame.transform.scale(background_two,(WIDTH,HEIGHT))

#PERSONAJE CACA
sprite= pygame.image.load("Recursos juego/caca.png")
nuevo_ancho = int(sprite.get_width() / 2)
nuevo_alto = int(sprite.get_height() / 2)
sprite= pygame.transform.scale(sprite, (nuevo_ancho, nuevo_alto))
class Personaje:
    def __init__(self, x, y,ancho_pantalla, alto_pantalla):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load("Recursos juego/pnn.png")
        self.velocidad = 10
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla
    def actualizar(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += self.velocidad
        elif keys[pygame.K_LEFT]:
            self.x -= self.velocidad
        elif keys[pygame.K_DOWN]:
            self.y += self.velocidad
        elif keys[pygame.K_UP]:
            self.y -= self.velocidad

        if self.x <= 0:
            self.x = 0
        elif self.x > self.ancho_pantalla - self.sprite.get_width():
            self.x = self.ancho_pantalla - self.sprite.get_width()

        if self.y <= 0:
            self.y = 0
        elif self.y > self.alto_pantalla - self.sprite.get_height():
            self.y = self.alto_pantalla - self.sprite.get_height()
    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, (self.x, self.y))

#VENTANA DE MOSTRAR OPCIONES
def empieza_juego():
    personaje = Personaje(100, 100,WIDTH,HEIGHT)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SCREEN_2.blit(background_two, (0, 0))
        personaje.actualizar()
        personaje.dibujar(SCREEN_2)
        pygame.display.flip()
        # Dibuja la ventana de opciones y sus componentes
        # Aquí puedes agregar botones, casillas de verificación, deslizadores, etc.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                empieza_juego()
                print("Boton presionado")
    PANTALLA.blit(background_image,(0,0))
    PANTALLA.blit(tittle_image,tittle_rect)
    PANTALLA.blit(button_image, button_rect)
    pygame.display.update()
    pygame.display.flip()
