import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana del juego
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Colores RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Tamaño del laberinto
MAZE_WIDTH = 40
MAZE_HEIGHT = 30

# Tamaño de cada celda del laberinto
CELL_WIDTH = WINDOW_WIDTH // MAZE_WIDTH
CELL_HEIGHT = WINDOW_HEIGHT // MAZE_HEIGHT

# Inicialización de la ventana del juego
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Laberinto")

clock = pygame.time.Clock()

# Clase para representar al jugador
class Player(pygame.sprite.Sprite):
    def _init_(self, x, y):
        super()._init_()
        self.image = pygame.Surface((CELL_WIDTH // 2, CELL_HEIGHT // 2))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Movimiento del jugador con las teclas de dirección
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= CELL_HEIGHT // 2
        elif keys[pygame.K_DOWN]:
            self.rect.y += CELL_HEIGHT // 2
        elif keys[pygame.K_LEFT]:
            self.rect.x -= CELL_WIDTH // 2
        elif keys[pygame.K_RIGHT]:
            self.rect.x += CELL_WIDTH // 2

        # Limitar el movimiento dentro del laberinto
        self.rect.x = max(0, min(self.rect.x, WINDOW_WIDTH - CELL_WIDTH // 2))
        self.rect.y = max(0, min(self.rect.y, WINDOW_HEIGHT - CELL_HEIGHT // 2))

# Generación del laberinto aleatorio
def generate_maze():
    maze = []
    for _ in range(MAZE_HEIGHT):
        row = []
        for _ in range(MAZE_WIDTH):
            row.append(random.choice([True, False]))  # Pared o pasillo
        maze.append(row)
    return maze

# Dibujar el laberinto en la ventana del juego
def draw_maze(maze):
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            cell = maze[y][x]
            color = BLACK if cell else WHITE
            pygame.draw.rect(window, color, (x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

# Inicialización del jugador
player = Player(CELL_WIDTH // 2, CELL_HEIGHT // 2)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Generación del laberinto
maze = generate_maze()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar el jugador
    all_sprites.update()

    # Limpiar la ventana del juego
    window.fill(BLACK)

    # Dibujar el laberinto y el jugador
    draw_maze(maze)
    all_sprites.draw(window)

    # Limitar la visión del jugador
    pygame.draw.rect(window, BLACK, (player.rect.x - CELL_WIDTH, player.rect.y - CELL_HEIGHT, CELL_WIDTH * 3, CELL_HEIGHT * 3))

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Finalizar Pygame
pygame.quit()