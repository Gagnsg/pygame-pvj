import pygame

#Iniciación de Pygame
pygame.init()

#Pantalla - ventana
W, H = 1000, 600
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Exterminator')
icono=pygame.image.load("D:\piton\Recursos juego\caca.png")
pygame.display.set_icon(icono)

#Fondo del juego
fondo = pygame.image.load("D:\piton\Recursos juego\Long spaceshi 0 (2).jpg")
fondo=pygame.transform.scale(fondo,(W,H))
"""#Música de fondo
pygame.mixer.music.load('sonido/intergalactic_odyssey.ogg')
pygame.mixer.music.play(-1)
"""

#Personaje
quieto = pygame.image.load("D:\piton\Recursos juego\SPRITES\QUIETO\AYUDA.png")

caminaIzquierda= [pygame.image.load("Recursos juego/SPRITES/CORRER IZQUIERDA/Pers_correr_izq_1.png"),
                   pygame.image.load("Recursos juego/SPRITES/CORRER IZQUIERDA/Pers_correr_izq_2.png"),
                   pygame.image.load("Recursos juego/SPRITES/CORRER IZQUIERDA/Pers_correr_izq_3.png"),
                   pygame.image.load("Recursos juego/SPRITES/CORRER IZQUIERDA/Pers_correr_izq_4.png"),
                   pygame.image.load("Recursos juego/SPRITES/CORRER IZQUIERDA/Pers_correr_izq_5.png"),
                  pygame.image.load("Recursos juego/SPRITES/CORRER IZQUIERDA/Pers_correr_izq_6.png")]

caminaDerecha= [pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_1.png"),
                pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_2.png"),
                pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_3.png"),
                pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_4.png"),
                pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_5.png"),
                pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_6.png")]

arriba = [pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_1.png"),
          pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_2.png"),
          pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_3.png"),
          pygame.image.load("Recursos juego/SPRITES/CORRER DERECHA/Pers_correr_4.png")]

"""#Sonido
sonido_arriba = pygame.image.load('sonido/volume_up.png')
sonido_abajo = pygame.image.load('sonido/volume_down.png')
sonido_mute = pygame.image.load('sonido/volume_muted.png')
sonido_max = pygame.image.load('sonido/volume_max.png')"""

x=0
px = 50
py = 200
ancho = 40
velocidad = 10

#Control de FPS
reloj = pygame.time.Clock()

#Contador de salto
cuentaSalto = 10

#Variables dirección
izquierda = False
derecha = False
arribo = False

#Pasos
cuentaPasos = 0

#Movimiento
def recargaPantalla():
    #Variables globales
    global cuentaPasos
    global x

    #Fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5
    #Contador de pasos
    if cuentaPasos + 1 >= 6:
        cuentaPasos = 0
    #Movimiento a la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1
        # Movimiento a la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    elif arribo + 1 >= 4:
        PANTALLA.blit(arriba[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    else:
        PANTALLA.blit(quieto,(int(px), int(py)))

ejecuta = True

#Bucle de acciones y controles
while ejecuta:
    #FPS
    reloj.tick(18)

    #Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    #Opción tecla pulsada
    keys = pygame.key.get_pressed()

    #Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False

    #Tecla D - Moviemiento a la derecha
    elif keys[pygame.K_d] and px <= 900 - velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True

    #Personaje quieto
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0

    #Tecla W - Moviemiento hacia arriba
    if keys[pygame.K_w] and py > 0:
        py -= velocidad
        arribo=True

    #Tecla S - Moviemiento hacia abajo
    if keys[pygame.K_s] and py < 460:
        py += velocidad


    # Actualización de la ventana
    pygame.display.update()
    #Llamada a la función de actualización de la ventana
    recargaPantalla()

#Salida del juego
pygame.quit()

"""# Control del audio
# Baja volumen
if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
    PANTALLA.blit(sonido_abajo, (850, 25))
elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
    PANTALLA.blit(sonido_mute, (850, 25))

# Sube volumen
if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
    PANTALLA.blit(sonido_arriba, (850, 25))
elif keys[pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
    PANTALLA.blit(sonido_max, (850, 25))

# Desactivar sonido
elif keys[pygame.K_m]:
    pygame.mixer.music.set_volume(0.0)
    PANTALLA.blit(sonido_mute, (850, 25))

# Reactivar sonido
elif keys[pygame.K_COMMA]:
    pygame.mixer.music.set_volume(1.0)
    PANTALLA.blit(sonido_max, (850, 25))"""