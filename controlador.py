# import pygame

from PyQt5 import QtWidgets
import sys

# Model
from modelo import Sistema, Run_game ,client

# View
from vista import Ventana, Ventana2

class comunicacion():
    def __init__(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        # Ventanas( Vista )
        self.__mainMenu = Ventana()
        self.__secondMenu = Ventana2()
        # Modelo
        self.__system = Sistema(client)
        self.__runGame = Run_game()
        ######
        self.controller = Controller(self.__mainMenu, self.__secondMenu, self.__system, self.__runGame)
        self.__mainMenu.conexionControlador(self.controller) 
        self.__secondMenu.conexionControlador(self.controller)
 
    def main(self): # el que se va a encargar de correr el codigo 
        self.__mainMenu.show()
        sys.exit(self.__app.exec_())

class Controller:
    def __init__(self, mainMenu, secondMenu ,system, runGame):
        self.__mainMenu = mainMenu
        self.__secondMenu = secondMenu
        self.__system = system
        self.__runGame = runGame

    def obtener_Nombre(self, cc):
        return self.__system.obtenerNombre(cc)
    
    def verificar_Cedula(self, cc):
        if self.__system.verificarCedula(cc):
            return True
        else:
            return False
            
    def agregarDatos(self, cc, name):
        self.__system.cedulaAsignar(cc)
        self.__system.nombreAsignar(cc, name)
    
    # Metodos para cambiar de ventana
    def cambiar_a_ventana2(self):
        self.__secondMenu.check_coord()
        self.__secondMenu.check_refle()
        self.__secondMenu.check_predic()
        self.__secondMenu.show()
        self.__mainMenu.close()
    
    def cambiar_a_ventana1(self):
        self.__mainMenu.show()
        self.__secondMenu.close()
    
    # Separé este método de run_third_one porque lo necesito (JUAN)
    def get_score_game(self, game):
        return self.__system.verificarScore(self.__mainMenu.cc, game)
    
    # Metodos para correr el codigo llamadado de la vista 
    def run_first_one(self):
        if self.get_score_game("Coordinacion") == None:
            self.__runGame = Run_game()
            self.__runGame.cordination_run()        
        if self.__system.verificarCedula(self.__mainMenu.cc) == True:
            self.__system.scoreAsignar(self.__mainMenu.cc, self.__runGame.getScore(), "Coordinacion")
        self.__secondMenu.showScore(self.__runGame.getScore())
        self.__secondMenu.check_coord()

    def run_second_one(self):
        if self.get_score_game("Reflejos") == None:
            self.__runGame = Run_game()
            self.__runGame.reflexes_run()        
        if self.__system.verificarCedula(self.__mainMenu.cc) == True:
            self.__system.scoreAsignar(self.__mainMenu.cc, self.__runGame.getScore(), "Reflejos")
        self.__secondMenu.showScore(self.__runGame.getScore())
        self.__secondMenu.check_refle()
    
    def run_third_one(self):
        if self.get_score_game("Prediccion de Velocidad") == None:
            self.__runGame = Run_game()
            self.__runGame.circle_run()
        if self.__system.verificarCedula(self.__mainMenu.cc) == True:
            self.__system.scoreAsignar(self.__mainMenu.cc, self.__runGame.getScore(), "Prediccion de Velocidad")
        self.__secondMenu.showScore(self.__runGame.getScore())
        self.__secondMenu.check_predic() 

    
if __name__ == "__main__":
    control = comunicacion()
    control.main()

