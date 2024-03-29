import pygame
import random 
import pymongo
import time


# Clases pymongo
client  = pymongo.MongoClient('mongodb+srv://josuepaniagua:Josue123@cluster0.megrtoc.mongodb.net/') # tengo que mirar mañana en la unversidad por que no me da 
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
        self.color = random.choice([self.red, self.green])
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


# Clases para el primer juego ( Prediccion de velocidad )
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

# Clases para el segundo juego( Coordinacion )
class Rectangle(General):
    def __init__(self):
        super().__init__()
        self.positions = [(250, 50)]
        self.side_a = 500
    def draw_rectangle(self, surface):
        for position in self.positions:
            pygame.draw.rect(surface, self.color, (position[0], position[1], self.side_a, self.side_a))
    
class StaticCircle(General):
    def __init__(self):
        super().__init__()
        self.positions = [(self.screen_width/2, self.screen_height/2)]
        self.circle_radius = 250
    def draw_static_circle(self, surface):
        for position in self.positions:
            pygame.draw.circle(surface, self.color, (position[0], position[1]), self.circle_radius)
    
# Clases para el tercer juego( Reflejos )
class Images(General):
    def __init__(self):
        super().__init__()
        self.imageWidth = 470
        self.imageHeight = 380
        self.positions = ([(self.screen_width - self.imageWidth) / 2, (self.screen_height - self.imageHeight) / 2])
    
# Clase para correr los juegos
class Run_game():
    def __init__(self):
        self.run = True
        self.game_over = False
        self.score = 0
        self.cont = 0

    # Metodos que nos van a servir en los resoectivos juegos
    def getScore(self):
        return self.score

    def timePassedScore(self, current_time):
        if current_time <= 2:
            self.score += 100
        elif 3 < current_time <= 4:
            self.score += 50
        
    def restartClock(self):
        self.initialClock = time.time()
        self.finalClock = time.time()

    def restarRandomClock(self):
        self.random_time_green = random.uniform(2, 5)    
        self.random_time_red = random.uniform(0.01, 0.04)              
    
    # JUEGO #1( Prediccion Velocidad )
    def circle_run(self):
        
        g = General() 
        c = Circle()
        s = Square()
        
        pygame.init()

        # Inicializar la pantalla y el reloj
        screen = pygame.display.set_mode( [g.screen_width, g.screen_height] )
        pygame.display.set_caption("Prediccion de Velocidad")
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
    

    # JUEGO #2 ( Coordinacion )
    def cordination_run(self):
        
        g = General()
        r = Rectangle()
        c = StaticCircle()

        # Iniciar el reloj
        self.initialClock = time.time()

        pygame.init()
        
        # Inicializar la pantalla 
        screen = pygame.display.set_mode( [g.screen_width, g.screen_height] )
        pygame.display.set_caption("Coordinacion")
        clock = pygame.time.Clock()

        shapes = [c, r]
        figure = random.choice(shapes)
        
        # Ciclo para que la pestalla se mantenga
        while self.run :

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.run = False 
                elif event.type == pygame.KEYDOWN:
                    # Letras que vamos a tener en cuenta
                    if event.key == pygame.K_w:# W para el rectangulo rojo
                        if figure == r and r.color == r.red:
                            self.timePassedScore(current_time)
                            self.restartClock()
                    elif event.key == pygame.K_a:# A para el rectangulo verde
                        if figure == r and r.color == r.green:
                            self.timePassedScore(current_time)
                            self.restartClock()
                    elif event.key == pygame.K_s :# S para el circulo rojo
                        if figure == c and  c.color == c.red:
                            self.timePassedScore(current_time)
                            self.restartClock()
                    elif event.key == pygame.K_d :# D para el circulo verde
                        if figure == c and c.color == c.green:
                            self.timePassedScore(current_time)
                            self.restartClock()
                    figure = random.choice(shapes)
                    r.color = random.choice([r.red, r.green])
                    c.color = random.choice([c.red, c.green])  
                    self.cont += 1 
                    
            # Rellenar la pantalla y añadir el texto del score
            screen.fill(g.white)
            g.draw_text(f'Score: {self.score}', screen, g.screen_width / 2, 15)

            # tiempo final y Tiempo transcurrido
            self.finalClock = time.time()
            current_time = self.finalClock - self.initialClock
            
            # Dibujar una figura al azar si transcurren 10seg sin presionar una tecla
            if current_time > 6:
                figure = random.choice(shapes)
                r.color = random.choice([r.red, r.green])
                c.color = random.choice([c.red, c.green])
                # Hay que volver a inicializar el tiempo 
                self.restartClock()
                self.cont += 1
                
            # Dibujar en pantalla dependiendo de la figura que elija el random
            if figure == c:
                figure.draw_static_circle(screen)
            elif figure == r:
                figure.draw_rectangle(screen)

            if self.cont > 10:
                self.run = False

            # Actualizar la pantalla
            pygame.display.update()
            clock.tick(60)

        pygame.quit()

    # JUEGO #3 ( Reflejos )
    def reflexes_run(self):
        
        g = General()
        i = Images()

        pygame.init()

        # Definir un tiempo aleatorio 
        self.initialClock = time.time()
        self.random_time_green = random.uniform(2, 5)    
        self.random_time_red = random.uniform(0.01, 0.04)   
            
        # Inicializar la pantalla y el reloj
        screen = pygame.display.set_mode( [g.screen_width, g.screen_height] )
        pygame.display.set_caption( "Reflejos" )
        clock = pygame.time.Clock()

        # Vamos a cargar las imagenes que vamos a usar
        greenLight = pygame.image.load( "imagenes\green_trafficLight.webp" )
        redLight = pygame.image.load( r"imagenes\red_trafficLight.jpg" )
        oldMan = pygame.image.load( r"imagenes\old_man.png" )
        pedestrianLight = pygame.image.load( r"imagenes\red_pedestrianLight.jpg" )
        # Transformar el tamaño de la imagen
        greenLight = pygame.transform.scale(greenLight, (i.imageWidth, i.imageHeight))
        redLight = pygame.transform.scale(redLight, (i.imageWidth, i.imageHeight))
        oldMan = pygame.transform.scale(oldMan, (i.imageWidth, i.imageHeight))
        pedestrianLight = pygame.transform.scale(pedestrianLight, (i.imageWidth - 10, i.imageHeight + 30))
        images = [greenLight, redLight, oldMan, pedestrianLight]
        # Usando la libreria random para elegir una imagen al azar
        image = random.choice( images )

        # Creamos el ciclo para que la pestalla se mantenga
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
            
            # Necesitamos que la tecla SPACE cuente si esta preionada
            keys = pygame.key.get_pressed()

            # Rellenar la pagina de un color determinado
            screen.fill(g.white) 
            g.draw_text(f"Score: {self.score}", screen, g.screen_width / 2, 15)

            # Tiempo final y actual 
            self.finalClock = time.time()
            current_time = self.finalClock - self.initialClock

            # Siguiendo con la logica de la tecla SPACE
            if keys[pygame.K_SPACE] : 
                if image == greenLight:
                    self.score += 0.5
                elif image == pedestrianLight:
                    self.score += 0.5
                elif image == oldMan:
                    self.score -= 2
                elif image == redLight:
                    self.score -= 2

            # Vamos a calcular el tiempo
            if image == greenLight or pedestrianLight:
                if current_time >= self.random_time_green:
                    image = random.choice( images )
                    self.restartClock()
                    self.restarRandomClock()
                    self.cont += 1
            elif image == redLight or oldMan :
                if current_time >= self.random_time_red:
                    image = random.choice( images )
                    self.restartClock()
                    self.restarRandomClock()

            # Mostrar la imagen elegida en el random
            if image == greenLight:
                screen.blit( greenLight, ((g.screen_width - i.imageWidth) / 2, (g.screen_height - i.imageHeight) / 2) )
            elif image == pedestrianLight:
                screen.blit( pedestrianLight, ((g.screen_width - i.imageWidth - 10) / 2, (g.screen_height - i.imageHeight + 30) / 2) )
            elif image == redLight:
                screen.blit( redLight, ((g.screen_width - i.imageWidth) / 2, (g.screen_height - i.imageHeight) / 2) )
            elif image == oldMan:
                screen.blit( oldMan, ((g.screen_width - i.imageWidth) / 2, (g.screen_height - i.imageHeight) / 2) )

            # Para detener el juego
            if self.cont > 7:
                self.run = False 
            
            # Actualizar la pantalla
            pygame.display.update()
            clock.tick(30)
        pygame.quit()