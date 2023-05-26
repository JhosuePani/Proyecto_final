# import pygame
# #from modelo import General, Circle, Square as g, c, s
# import modelo as md

# # Clases
# # Datos principales 
# SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 600
# CIRCLE_SPEED = 2
# CIRCLE_RADIUS = 20
# SQUARE_L = 230

# # Colores
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)


# # PYGAME
# pygame.init()

# screen = pygame.display.set_mode( [SCREEN_WIDTH, SCREEN_HEIGHT] )
# pygame.display.set_caption("Circulo")

# clock = pygame.time.Clock()


# circle = md.Circle()
# square = md.Square()
# run = True
# game_over = False
# score = 0
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             run = False
#         # Usando el teclado
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_r:
#                 circle.direction = "S" # Para que pare en la posicion en que este cuando presione la tecla
#                 circle = md.Circle()
#                 square = md.Square()
#                 game_over = False

#     if game_over == False:
#         # Mover el circulo 
#         circle.move()
#         square.location(circle.direction[0])

#         if circle.positions[0][0] < 0 or circle.positions[0][0] > SCREEN_WIDTH - 10:
#             game_over = True
#         elif circle.positions[0][1] < square.positions[0][1]:
#             game_over = True
#         for position in circle.positions[1:]:
#             if circle.positions[0] == position:
#                 game_over = True

#     # Dibujos de la pantalla
#     screen.fill(WHITE)
#     circle.draw(screen)
#     square.draw_square(screen)

#     # Actualizar la pantalla 
#     pygame.display.update()
#     clock.tick(60)

# pygame.quit()


from PyQt5 import QtWidgets
import sys

# Model
from modelo import Sistema, client

# View
from vista import Ventana

class comunicacion():
    def __init__(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__view = Ventana()
        self.__system = Sistema(client)
        self.controller = controller(self.__view, self.__system)
        self.__view.conexionControlador(self.controller) 
 
    def main(self): # el que se va a encargar de correr el codigo 
        self.__view.show()
        sys.exit(self.__app.exec_())

class controller():
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    def verificarDatos(self, cc):
        nombre = self.__model.cedulaVerificar(cc)
        if nombre != None:
            pass
            #self.__view.rellenarDatos(nombre)
        else:
            pass
            # QMessageBox.about(self, "Alerta", "Esta cédula ya está registrada, ¿está seguro de cambiar el nombre? Una vez cambiado el nombre los datos se reiniciarán")

    def agregarDatos(self, cc, name):
        self.__model.cedulaAsignar(cc)
        self.__model.nombreAsignar(cc, name)

if __name__ == "__main__":
    control = comunicacion()
    control.main()

