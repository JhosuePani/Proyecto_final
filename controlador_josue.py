import pygame
#from modelo import General, Circle, Square as g, c, s


class Run_game():
    def __init__(self, General, Circle, Square):
        self.run = True
        self.game_over = False

    def circle_run(self, general, circle, square):
        pygame.init()

        screen = pygame.display.set_mode( [general.screen_width, general.screen_height] )
        pygame.display.set_caption("Circulo")
        clock = pygame.time.Clock()

        while self.run:
            for event in pygame.event.get():
                pass




def mifun(General,Circle,Square):
    

    # pygame
    pygame.init()

    font = pygame.font.SysFont( "Times New Roman", 25 )
    score = 0
    a = 0

    def draw_text(text, font, surface, x, y): # Creamos este para poder dibujar texto 
        text_object = font.render(text, True, BLACK)  # el render es especifico de pygame para añadir texto en las pantallas
        text_rect = text_object.get_rect() 
        text_rect.center = (x, y)
        surface.blit(text_object, text_rect)

    screen = pygame.display.set_mode( [SCREEN_WIDTH, SCREEN_HEIGHT] )
    pygame.display.set_caption("Circulo")

    clock = pygame.time.Clock()


    circle = Circle
    square = Square


    run = True
    game_over = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            # Usando el teclado
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if (circle.positions[0][0] - CIRCLE_RADIUS) == square.positions[0][0] and circle.direction == "L":
                        score += 100
                    elif (circle.positions[0][0] + CIRCLE_RADIUS) == (square.positions[0][0] + 230) and circle.direction == "R":
                        score += 100
                    elif square.positions[0][0] - 8 <= circle.positions[0][0] <= square.positions[0][0] + 8  and circle.direction == "L":
                        score += 60
                    elif square.positions[0][0] - 222 <= circle.positions[0][0] <= square.positions[0][0] + 238  and circle.direction == "R":
                        score += 60
                    elif square.positions[0][0] - 16 <= circle.positions[0][0] <= square.positions[0][0] + 16  and circle.direction == "L":
                        score += 20
                    elif square.positions[0][0] - 214 <= circle.positions[0][0] <= square.positions[0][0] + 246  and circle.direction == "R":
                        score += 20
                    circle = Circle
                    square = Square
                    game_over = False
                    a += 1
                elif event.key == pygame.K_t and game_over == True:
                    circle = Circle
                    square = Square
                    score = 0
                    a = 0
                    game_over = False


        if game_over == False:
            # Mover el circulo 
            circle.move()
            square.location(circle.direction[0])

            if circle.positions[0][0] < 0 or circle.positions[0][0] > SCREEN_WIDTH - 10:
                game_over = True
            for position in circle.positions[1:]:
                if circle.positions[0] == position:
                    game_over = True


        # Dibujos de la pantalla
        screen.fill(WHITE)
        draw_text("Score: {}".format(score), font, screen, SCREEN_WIDTH/2, 10)
        circle.draw(screen)
        square.draw_square(screen)

        if a > 6:
            draw_text("PRUEBA FINALIZADA, Presione la tecla T para reiniciar", font, screen, SCREEN_WIDTH/2, SCREEN_HEIGHT / 2)
            game_over = True

        # Actualizar la pantalla 
        pygame.display.update()
        clock.tick(60)

    pygame.quit()