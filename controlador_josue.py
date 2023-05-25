import pygame
import numpy as np
#from modelo import General, Circle, Square as g, c, s
import modelo as md

# Clases
# Datos principales 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
CIRCLE_SPEED = 2
CIRCLE_RADIUS = 20
SQUARE_L = 230

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = 

def add_text(text, ):


# PYGAME
pygame.init()

screen = pygame.display.set_mode( [SCREEN_WIDTH, SCREEN_HEIGHT] )
pygame.display.set_caption("Circulo")

clock = pygame.time.Clock()


circle = md.Circle()
square = md.Square()
run = True
game_over = False
score = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        # Usando el teclado
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                circle.direction = "S" # Para que pare en la posicion en que este cuando presione la tecla
                circle = md.Circle()
                square = md.Square()
                game_over = False

    if game_over == False:
        # Mover el circulo 
        circle.move()
        square.location(circle.direction[0])

        if circle.positions[0][0] < 0 or circle.positions[0][0] > SCREEN_WIDTH - 10:
            game_over = True
        # elif circle.positions[0][0] < square.positions[0][0] and circle.direction[0] == "L":
        #     game_over = True
        # elif circle.positions[0][0] > (square.positions[0][0] + SQUARE_L) and circle.direction[0] == "R":
        #     game_over = True
        for position in circle.positions[1:]:
            if circle.positions[0] == position:
                game_over = True

    print(circle.positions[0])
    # Dibujos de la pantalla
    screen.fill(WHITE)
    circle.draw(screen)
    square.draw_square(screen)

    # Actualizar la pantalla 
    pygame.display.update()
    clock.tick(60)

pygame.quit()