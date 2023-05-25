from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class Ventana(QtWidgets.QMainWindow): # La clase ventana herreda de QWitgets.QMainWindows
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self) #Estoy llamando al constructro de la clase que herede
        uic.loadUi(r'vistas\main_menu.ui', self) # estoy cargando el archivo de Qtdesign con el que voy a trabajar

        # Vamos a conectar los botones
        #self.verifica = QtWidgets.QPushButton(self)
        self.IngresarBoton.clicked.connect( self.verificar_dato )
        self.IngresarBoton.clicked.connect( self.agregar_dato )

    def conexionControlador(self, control):
        self.controlador = control

    def agregar_dato(self):
        cedula = self.cedula_celda.text()
        if cedula.isdigit():
            self.controlador.agregarDatos(cedula, self.nombre_celda.text())
            self.abrirVentanaSecundaria()
        else:
            QMessageBox.about(self, "Alerta", "La cédula solo puede contener numeros..." )

    def verificar_dato(self):
        self.controlador.verificarDatos(self.cedula_celda.text())

    def rellenarDatos(self, nombre):
        self.nombre_celda.setText(nombre)
    
    def abrirVentanaSecundaria(self):
        self.hide()
        ventana2 = Ventana2()
        ventana2.show()


class Ventana2(QtWidgets.QMainWindow): # La clase ventana herreda de QWitgets.QMainWindows
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self) #Estoy llamando al constructro de la clase que herede
        uic.loadUi(r'Final/vistas/selec_menu.ui', self) # estoy cargando el archivo de Qtdesign con el que voy a trabajar

        # Vamos a conectar los botones
        #self.verifica = QtWidgets.QPushButton(self)
        self.IngresarBoton.clicked.connect( self.verificar_dato )
        self.IngresarBoton.clicked.connect( self.agregar_dato )

    def conexionControlador(self, control):
        self.controlador = control

    def agregar_dato(self):
        cedula = self.cedula_celda.text()
        if cedula.isdigit():
            self.controlador.agregarDatos(cedula, self.nombre_celda.text())
        else:
            QMessageBox.about(self, "Alerta", "La cédula solo puede contener numeros..." )

    def verificar_dato(self):
        self.controlador.verificarDatos(self.cedula_celda.text())

    def rellenarDatos(self, nombre):
        self.nombre_celda.setText(nombre)
        