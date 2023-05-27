import pygame
import random 
import pymongo


# Clases pymongo
client  = pymongo.MongoClient('mongodb+srv://josuepaniagua:Ba123@cluster0.megrtoc.mongodb.net/') # tengo que mirar mañana en la unversidad por que no me da 
db = client.test    

class Sistema:
    def __init__(self, client):
        mydb = client["Condumás"]
        self.__paciente = mydb["Resultados"]

    def nombreObtener(self, cc):
        pass
    
    def cedulaAsignar(self, cc):
        self.__paciente.insert_one({'Cedula': cc})
    
    def nombreAsignar(self, cc, nombre):
        doc = {'Cedula': cc}
        name = {'$set': {'Nombre': nombre}}
        self.__paciente.update_one(doc, name)
    
    def obtenerNombre(self, cc):
            documento = self.__paciente.find_one({'Cedula': cc})
            return documento.get('Nombre')

    def verificarNombre(self, nomb):
        nombre = self.__paciente.find_one({'Nombre': nomb})
        if nombre != None:
            return True
        else:
            return False
    
    def verificarCedula(self, cc):
        cedula = self.__paciente.find_one({'Cedula': cc})
        if cedula == None:
            return False
        else:
            return True
        
    def verificarScore(self, cc, game):
        documento = self.__paciente.find_one({'Cedula': cc})
        return documento.get(f'Score_{game}')

    def scoreAsignar(self, cc, score, game):
        doc = {'Cedula': cc}
        sco = {'$set': {f'Score_{game}': score}}
        self.__paciente.update_one(doc, sco)

# Clases de pygame
class General:
    def __init__(self):
        # colores 
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        # Label
        pygame.init()
        self.font = pygame.font.SysFont( "Times New Roman", 25 )
        # Tamaño ventana
        self.screen_width = 1000
        self.screen_height = 600
    def draw_text(self, text, surface, x, y):
        text_object = self.font.render(text, True, self.black)  # el render es especifico de pygame para añadir texto en las pantallas
        text_rect = text_object.get_rect() 
        text_rect.center = (x, y)
        surface.blit(text_object, text_rect)


class Circle(General):
    def __init__(self):
        super().__init__()
        self.positions = [(self.screen_width / 2, 200 + 230)]
        self.direction = random.choice(["R", "L"])
        self.circle_radius = 20
        self.circle_speed = 2
    def move(self):
        x, y = self.positions[0]
        if self.direction[0] == "R":
            x += self.circle_speed
        elif self.direction[0] == "L":
            x -= self.circle_speed
        self.positions.insert(0, (x, y))
        self.positions.pop()
    def draw(self, surface):
        for position in self.positions:
            pygame.draw.circle(surface, self.green, (position[0], position[1]), self.circle_radius)

class Square(General):
    def __init__(self):
        super().__init__()
        self.positions = [(0, 200 + 20)]
        self.square_l = 230
    def location(self, direction):
        x, y = self.positions[0]
        if direction == "R":
            x = 670
        elif direction == "L":
            x = 100 
        self.positions.insert(0, (x, y))
        self.positions.pop()      
    def draw_square(self, surface): 
        for position in self.positions:
            pygame.draw.rect(surface, self.red, (position[0], position[1], self.square_l, self.square_l))
    

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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: # ACA ESTA EL PROBLAM DE LO DEL SCORE
                        if (c.positions[0][0] - c.circle_radius) == s.positions[0][0] and c.direction == "L":
                            self.score += 100
                        elif (c.positions[0][0] + c.circle_radius) == (s.positions[0][0] + 230) and c.direction == "R": # aca
                            self.score += 100
                        elif s.positions[0][0] - 8 <= c.positions[0][0] <= s.positions[0][0] + 8  and c.direction == "L":
                            self.score += 60
                        elif s.positions[0][0] + 222 <= c.positions[0][0] <= s.positions[0][0] + 238  and c.direction == "R": # aca
                            self.score += 60
                        elif s.positions[0][0] - 16 <= c.positions[0][0] <= s.positions[0][0] + 16  and c.direction == "L":
                            self.score += 20
                        elif s.positions[0][0] + 214 <= c.positions[0][0] <= s.positions[0][0] + 246  and c.direction == "R": # aca
                            self.score += 20
                        g = General() 
                        c = Circle()
                        s = Square()
                        self.cont += 1
                                
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
                g.draw_text("PRUEBA FINALIZADA", screen, g.screen_width/2, g.screen_height/2)
                self.game_over = True
                self.run = False
            # Actualizar la pantalla
            pygame.display.update()
            clock.tick(60)
        
        pygame.quit()

    def getScore(self):
        return self.score

