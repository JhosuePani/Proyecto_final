

import pygame

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
width, height = 400, 300

# Crear la ventana
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cronómetro")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fuente
font = pygame.font.Font(None, 50)

# Variables del cronómetro
elapsed_time = 0
running = False

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running

    # Actualizar el cronómetro si está en ejecución
    if running:
        elapsed_time += pygame.time.get_ticks() // 1000

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Mostrar el tiempo transcurrido en el cronómetro
    timer_text = font.render(str(elapsed_time), True, WHITE)
    screen.blit(timer_text, (width // 2 - timer_text.get_width() // 2, height // 2 - timer_text.get_height() // 2))

    # Actualizar la pantalla
    pygame.display.flip()

