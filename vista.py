from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import imagenes.wallpaper

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('imagenes\main_menu.ui', self)
        
        self.IngresarBoton.clicked.connect( self.verificar_dato )
        self.IngresarBoton.clicked.connect( self.abrirVentana2 )

        self.cc = ''
        self.nombre = ''

        # Este atributo solo retorna True cuando la cédula y nombre
        # no están vacios en la ventana
        self.info_completa = False

    def conexionControlador(self, control):
        self.controlador = control

    def verificar_dato(self):      
        if self.controlador.verificar_Cedula(self.cedula_celda.text()):
            if self.controlador.obtener_Nombre(self.cedula_celda.text()) == self.nombre_celda.text():
                self.cc = self.cedula_celda.text()
                self.nombre = self.nombre_celda.text()
                self.info_completa = True
            else:
                QMessageBox.about(self, "Alerta", "La cédula ya está registrada, ingrese el mismo nombre")
        else:
            self.agregar_dato()

    def agregar_dato(self):
        self.cc = self.cedula_celda.text()
        self.nombre = self.nombre_celda.text()
        if self.cc != '' and self.nombre != '':
            if self.cc.isdigit():
                self.controlador.agregarDatos(self.cc, self.nombre_celda.text())
                self.info_completa = True
            else:
                QMessageBox.warning(self, "Alerta", "La cédula solo puede contener números.",
                                    QMessageBox.Ok)
        else:
             QMessageBox.warning(self, "Alerta", "Ingrese todos los datos.",
                                    QMessageBox.Ok)
    

    def abrirVentana2(self):
        if self.info_completa:
            self.controlador.cambiar_a_ventana2()
            self.info_completa = False


class Ventana2(QtWidgets.QMainWindow): # La clase ventana herreda de QWitgets.QMainWindows
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self) #Estoy llamando al constructro de la clase que herede
        uic.loadUi(r'imagenes/selec_menu.ui', self) # estoy cargando el archivo de Qtdesign con el que voy a trabajar

        # Vamos a conectar los botones
        #self.verifica = QtWidgets.QPushButton(self)
        self.coordBoton.clicked.connect( self.run_first ) # Coordinacion
        self.refleBoton.clicked.connect( self.run_second ) # Reflejos
        self.predicBoton.clicked.connect( self.run_third ) # Prediccion velocidad
        self.bBoton.clicked.connect( self.goBack )

    def conexionControlador(self, control):
        self.controlador = control
    
    ### Estos métodos establecen el check si un juego ya tiene su puntaje ###
    
    def check_coord(self):
        if self.controlador.get_score_game("Coordinacion") != None:
            self.checkCOORD.setChecked(True)
        else:
            self.checkCOORD.setChecked(False)

    def check_refle(self):
        if self.controlador.get_score_game("Reflejos") != None:
            self.checkREFLE.setChecked(True)
        else:
            self.checkREFLE.setChecked(False)

    def check_predic(self):
        if self.controlador.get_score_game("Prediccion de Velocidad") != None:
            self.checkPREDI.setChecked(True)
        else:
            self.checkPREDI.setChecked(False)
    

    ### metodos de ejecución de las pruebas ###

    def run_first(self): # Coordinacion
        self.controlador.run_first_one()
    
    def run_second(self): # Reflejos
        self.controlador.run_second_one()

    def run_third(self): # Prediccion de velocidad
        self.controlador.run_third_one()
    
    def goBack(self):
        self.controlador.cambiar_a_ventana1()
    
    def showScore(self, score):
        score = str(score)
        QMessageBox.about(self, "SCORE", "El Score obtenido fue: " + score)