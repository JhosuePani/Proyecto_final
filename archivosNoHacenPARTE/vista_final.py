# Respuesta grafica 
# importamos 1as Librerías necesarias
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
# Carga la interfaz gráfica y conecta los botones

# class ingreso(QtWidgets.QMainWindow):
#     '''Esta es la clase principal'''
#     # Inicializanos la ventana y conectanos los botones
#     def __init__(self):
#         # Inicializa la ventana
#         QtWidgets.QMainWindow.__init__(self)
#         uic.loadUi("ventanaMedico.ui", self)

class VentanaPrincipal(QtWidgets.QMainWindow):
    '''Esta es la clase principal''' 
    # Inicializanos la ventana y conectanos los botones
    def __init__(self):
        # Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("ventanaPrincipal.ui", self) # Lee el archivo de QtDesigner


        #self.admin.clicked.connect(self.abrirADMIN)
        self.medico.clicked.connect(self.abrirMEDICO)
        #self.paciente.clicked.connect(self.abrirPACIENTE)

    def conexionconelcontrolador(self, control):
        self.mi_controlador = control

    def abrirADMIN(self):
        self.mi_controlador.cambiarPrin_Med() 

    def abrirMEDICO(self):
        self.mi_controlador.cambiarPrin_Med() 

    def abrirPACIENTE(self):
        self.mi_controlador.cambiarPrin_Pac() 


        
class VentanaMed(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    # Inicializanos la ventana y conectanos los botones
    def __init__(self):
        # Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("ventanaMedi.ui", self) # Lee el archivo de QtDesigner
    
    # Conectar botones a funciones
        
        self.historiaClinica.clicked.connect(self.abrirHC)
        self.consuPaciente.clicked.connect(self.abrirCP)
        self.medicamento.clicked.connect(self.abrirMD)
        self.exit.clicked.connect(self.cerrar)
        
    def conexionconelcontrolador(self, control):
        self.mi_controlador = control

    def agregar_dato(self):
        self.mi_controlador.agregarPacientes(self.input_cedula.text(), self.input_nombre.text(), self.input_edad.text())
        self.agregar.setEnabled(False)
        self.continuar.setEnabled(True)
    def setup(self):
        self.input_cedula.setValidator(QIntValidator())
        self.input_nombre.setValidator(QRegExp())
        self.input_edad.setValidator(QIntValidator())

    def rellenarDatos(self, nombre, edad):
        self.input_nombre.setText(nombre)
        self.input_edad.setText(str(edad))
        self.verificar.setEnabled(False)
    
    def cerrar(self):
        self.close()

    def continuar_dato(self):
        print("menu_grafica")

    def abrirHC(self):
        self.mi_controlador.cambiarMed_HC() 

    def abrirCP(self):
        self.mi_controlador.cambiarMed_CP()

    def abrirMD(self):
        self.mi_controlador.cambiarMed_MD()
        
class historiaClinica(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("ventanaH_C.ui", self) 


        self.verificar_bd.clicked.connect(self.verificar_cedula)
        self.guardar_HC.clicked.connect(self.asignar_HC)
        self.exit_HC.clicked.connect(self.cerrar_HC)
        self.input_hisCli.setEnabled(False)
        self.guardar_HC.setEnabled(False)

    def conexionconelcontrolador(self, control):
        self.mi_controlador = control

    def verificar_cedula(self):
        x = self.mi_controlador.buscarensistema(self.input_cedulaPac.text()) 
        if x == True:
            self.input_hisCli.setEnabled(True)
            self.guardar_HC.setEnabled(True)
            print("vamos")

    def asignar_HC(self):
        self.mi_controlador.Guardar_HC(self.input_cedulaPac.text(),self.input_hisCli.toPlainText())

        msj= QMessageBox(self)
        msj.setIcon(QMessageBox.Information)
        msj.setText("historia clinica ingresada con exito!!!")
        msj.show() 

        self.abrirMed()    

    def cerrar_HC(self):
        self.close()    

    def abrirMed(self):
        self.mi_controlador.cambiarHC_Med()  

class ventanaConsultarPaciente(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("ventanaConsultarPac.ui", self) 

        self.consultar_pac.clicked.connect(self.consPac)
        self.return_consPac.clicked.connect(self.abrirMed)
        self.exit_CP.clicked.connect(self.cerrar_CP)

    def conexionconelcontrolador(self, control):
        self.mi_controlador = control

    def consPac(self):
        x = self.mi_controlador.buscarensistemaCP(self.input_cedPac.text()) 
        print(x)
        if x != None:
            msj= QMessageBox(self)
            msj.setIcon(QMessageBox.Information)
            msj.setText(f"Cédula del paciente: {x[0]['Cedula']}\n Nombre del paciente: {x[0]['Nombre']}\n Edad del paciente: {x[0]['Edad']}\n Historia clinica: {x[0]['Historia clinica']}")
            msj.show() 

    def cerrar_CP(self):
        self.close()    

    def abrirMed(self):
        self.mi_controlador.cambiarCP_Med()



class ventanaMedicamento(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("ventanaMedicamento.ui", self) 


        self.verificar_bdMed.clicked.connect(self.verificar_cedulaMD)
        self.guardar_Medica.clicked.connect(self.asignar_MD)
        self.exit_Medica.clicked.connect(self.cerrar_MD)
        self.input_Medicamentos.setEnabled(False)
        self.guardar_Medica.setEnabled(False)

    def conexionconelcontrolador(self, control):
        self.mi_controlador = control

    
    def verificar_cedulaMD(self):
        x = self.mi_controlador.buscarensistemaMD(self.input_cedulaPacMed.text()) 
        if x == True:
            self.input_Medicamentos.setEnabled(True)
            self.guardar_Medica.setEnabled(True)
            print("vamos")

    def asignar_MD(self):
        self.mi_controlador.Guardar_MD(self.input_cedulaPacMed.text(),self.input_Medicamentos.toPlainText())

        msj= QMessageBox(self)
        msj.setIcon(QMessageBox.Information)
        msj.setText("Medicamentos guardados con éxito!!!")
        msj.show() 

    def cerrar_MD(self):
        self.close()    

    def abrirMed(self):
        self.mi_controlador.cambiarMD_Med()  


