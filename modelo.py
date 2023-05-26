import pygame
import random 
import pymongo

# Clases pymongo
#client  = pymongo.MongoClient('mongodb+srv://josuepaniagua:Ba123@cluster0.megrtoc.mongodb.net/') # tengo que mirar mañana en la unversidad por que no me da 
#db = client.test    

class Sistema:
    def __init__(self, client):
        mydb = client["Condumás"]
        self.__paciente = mydb["Resultados"]
    
    def cedulaAsignar(self, cc):
        self.__paciente.insert_one({'Cedula': cc})
 
    def nombreAsignar(self, cc, nombre):
        doc = {'Cedula': cc}
        name = {'$set': {'Nombre': nombre}}
        self.__paciente.update_one(doc, name)
    
    def cedulaVerificar(self, cc):
        paciente = self.__paciente.find_one({'Cedula': cc})
        if paciente != None:
            return paciente['Nombre']
        else:
            return None
    
    def scoreAsignar(self, cc, score): # Juanjo este metodo lo asigne para que podamos conectar eso de tal manera que se guarde el score
        doc = {'Cedula': cc}
        sco = {'$set': {'Score': score}}
        self.__paciente.update_one(doc, sco)

# Clases de pygame
class General:
    def __init__(self):
        # colores 
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)

        # Tamaño ventana
        self.screen_width = 1000
        self.screen_height = 600
        # Radio del circulo 
        self.circle_radius = 20

class Circle(General):
    def __init__(self):
        super().__init__()
        self.positions = [(self.screen_width / 2, self.screen_height / 2)]
        self.direction = random.choice(["R", "L"])
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
        self.square_l = 230
        self.positions = [(0, (self.screen_height/2) - self.square_l + self.circle_radius)]
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

# Para añadir texto en la ventana de pygame
def draw_text(text, font, surface, x, y): # Creamos este para poder dibujar texto 
    text_object = font.render(text, True, (0, 0, 0))  # el render es especifico de pygame para añadir texto en las pantallas
    text_rect = text_object.get_rect() 
    text_rect.center = (x, y)
    surface.blit(text_object, text_rect)