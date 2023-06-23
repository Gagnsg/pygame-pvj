import pygame, sys
from pygame.locals import*
pygame.init()
#Conf. pantalla
W= 1160
H=650
#MEDIDAS CENTRO
cen=W/2
al=H/2
PANTALLA= pygame.display.set_mode((W, H))
#MTítulo, ícono y fondo
pygame.display.set_caption('Jueguito miado')
icon=pygame.image.load("Recursos juego/caca.png")
pygame.display.set_icon(icon)
#FONDO PANTALLA DE INICIO
background_image=pygame.image.load("Recursos juego/ondo.jpg")
background_image=pygame.transform.scale(background_image,(W,H))

#IMAGEN DE TÍTULO
tittle_image=pygame.image.load("Recursos juego/titulo_preview.png")
tittle_image=pygame.transform.scale(tittle_image, (W,H))
tittle_rect= tittle_image.get_rect()
tittle_rect.center= (cen,al)

#CREANDO EL BOTÓN
button_image= pygame.image.load("Recursos juego/inicio-PhotoRoom.png-PhotoRoom.png")
button_image=pygame.transform.scale(button_image, (200,100))
button_rect=button_image.get_rect()
button_rect.center=(cen,al+140)

#SCREEN 2
#Fondo del juego
fondo = pygame.image.load("D:\piton\Recursos juego\ondo.jpg")
fondo=pygame.transform.scale(fondo,(W,H))

#PERSONAJE CACA
sprite= pygame.image.load("Recursos juego/caca.png")
nuevo_ancho = int(sprite.get_width() / 2)
nuevo_alto = int(sprite.get_height() / 2)
sprite= pygame.transform.scale(sprite, (nuevo_ancho, nuevo_alto))
class Personaje:
    def __init__(self):
        self.quieto = pygame.image.load("D:\piton\Recursos juego\SPRITES\QUIETO\AYUDA.png")

        self.caminaIzquierda = [pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER IZQUIERDA\Pers_correr_izq_1.png"),
                           pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER IZQUIERDA\Pers_correr_izq_2.png"),
                           pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER IZQUIERDA\Pers_correr_izq_3.png"),
                           pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER IZQUIERDA\Pers_correr_izq_4.png"),
                           pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER IZQUIERDA\Pers_correr_izq_5.png"),
                           pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER IZQUIERDA\Pers_correr_izq_6.png")]

        self.caminaDerecha = [pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER DERECHA\Pers_correr_1.png"),
                         pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER DERECHA\Pers_correr_2.png"),
                         pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER DERECHA\Pers_correr_3.png"),
                         pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER DERECHA\Pers_correr_4.png"),
                         pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER DERECHA\Pers_correr_5.png"),
                         pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER DERECHA\Pers_correr_6.png")]

        self.salta = [pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER DERECHA\Pers_correr_1.png"),
                 pygame.image.load("D:\piton\Recursos juego\SPRITES\CORRER DERECHA\Pers_correr_2.png")]
        self.x = 0
        self.px = 50
        self.py = 200
        self.ancho = 40
        self.velocidad = 10

        # Control de FPS
        self.reloj = pygame.time.Clock()

        # Variables salto
        self.salto = False
        # Contador de salto
        self.cuentaSalto = 10

        # Variables dirección
        self.izquierda = False
        self.derecha = False

        # Pasos
        self.cuentaPasos = 0
        self.ejecuta = True
    def recargaPantalla(self):
        # Variables globales
        global cuentaPasos
        global x
        x=0
        cuentaPasos=0
        # Fondo en movimiento
        x_relativa = x % fondo.get_rect().width
        PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
        if x_relativa < W:
            PANTALLA.blit(fondo, (x_relativa, 0))
        x -= 5
        # Contador de pasos
        if cuentaPasos + 1 >= 5:
            cuentaPasos = 0
        # Movimiento a la izquierda
        if self.izquierda:
            PANTALLA.blit(self.caminaIzquierda[cuentaPasos // 1], (int(self.px), int(self.py)))
            cuentaPasos += 1

            # Movimiento a la derecha
        elif self.derecha:
            PANTALLA.blit(self.caminaDerecha[cuentaPasos // 1], (int(self.px), int(self.py)))
            cuentaPasos += 1

        elif self.salto + 1 >= 2:
            PANTALLA.blit(self.salta[cuentaPasos // 1], (int(self.px), int(self.py)))
            cuentaPasos += 1

        else:
            PANTALLA.blit(self.quieto, (int(self.px), int(self.py)))

    def acciones(self):
    # Bucle de acciones y controles
       while self.ejecuta:
         self.reloj.tick(18)

         for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                ejecuta = False

            if keys[pygame.K_a] and self.px > self.velocidad:
              self.px -= self.velocidad
              izquierda = True
              derecha = False

             # Tecla D - Moviemiento a la derecha
            elif keys[pygame.K_d] and self.px <= 900 - self.velocidad - self.ancho:
               self.px += self.velocidad
               izquierda = False
               derecha = True

               # Personaje quieto
            else:
              izquierda = False
              derecha = False
              cuentaPasos = 0

            # Tecla W - Moviemiento hacia arriba
            if keys[pygame.K_w] and self.py > 5:
              self.py -= self.velocidad

            if keys[pygame.K_s] and self.py < 460:
                self.py += self.velocidad
    pygame.display.update()
    recargaPantalla(self)


#VENTANA DE MOSTRAR OPCIONES
def empieza_juego():
    personaje = Personaje()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        fondo.blit(fondo, (0, 0))
        personaje.recargaPantalla()
        personaje.acciones()
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