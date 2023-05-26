import pygame
from modelo import General, Circle, Square

class Run_game():
    def __init__(self):
        self.run = True
        self.game_over = False
        self.score = 0
        self.cont = 0

    # JUEGO #1( Prediccion Velocidad )
    def circle_run(self):
        
        g = General() 
        c = Circle()
        s = Square()
        
        pygame.init()

        screen = pygame.display.set_mode( [g.screen_width, g.screen_height] )
        pygame.display.set_caption("Circulo")
        clock = pygame.time.Clock()

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.run = False
                elif event.time == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        if (c.positions[0][0] - c.circle_radius) == s.positions[0][0] and c.direction == "L":
                            self.score += 100
                        elif (c.positions[0][0] + c.circle_radius) == (s.positions[0][0] + 230) and c.direction == "R":
                            self.score += 100
                        elif s.positions[0][0] - 8 <= c.positions[0][0] <= s.positions[0][0] + 8  and c.direction == "L":
                            self.score += 60
                        elif s.positions[0][0] - 222 <= c.positions[0][0] <= s.positions[0][0] + 238  and c.direction == "R":
                            self.score += 60
                        elif s.positions[0][0] - 16 <= c.positions[0][0] <= s.positions[0][0] + 16  and c.direction == "L":
                            self.score += 20
                        elif s.positions[0][0] - 214 <= c.positions[0][0] <= s.positions[0][0] + 246  and c.direction == "R":
                            score += 20
                        g = General()
                        c = Circle()
                        s = Square()
                        self.cont += 1
                    elif event.key == pygame.K_t and self.game_over == True:
                        g = General()
                        c = Circle()
                        s = Square()
                        self.score = 0
                        self.cont = 0
                        self.game_over = False
            
            if self.game_over == False:

                c.move()
                s.location( c.direction[0] )

                if c.positions[0][0] < 0 or c.positions[0][0] > g.screen_width - 10:
                    self.game_over = True
                for position in c.positions[1:]:
                    if c.positions[0] == position:
                        self.game_over = True
            
            # Dibujar en la pantalla
            screen.fill(g.white)
            g.draw_text(f'Score: {self.score}', screen, g.screen_width / 2, 15)
            c.draw(screen)
            s.draw_square(screen)

            if self.cont > 6:
                g.draw_text("PRUEBA FINALIZADA, Presione la tecla T para reiniciar", screen, g.screen_width/2, g.screen_heigth/2)
                self.game_over = True
            
            # Actualizar la pantalla
            pygame.display.update()
            clock.tick(60)
        
        pygame.quit()

run = Run_game()
run.circle_run()
