from PyQt5 import QtWidgets
import sys

# Modelo
from modelo_final import Sistema, client

# Vista
from vista_final import VentanaMed,historiaClinica,ventanaConsultarPaciente,ventanaMedicamento,VentanaPrincipal



class comunicacion(object):
    def __init__ (self): 
        self.__app = QtWidgets.QApplication(sys.argv)
        self.ventanaPrin = VentanaPrincipal()
        self.__view = VentanaMed()
        self.ventanaHC = historiaClinica()
        self.system = Sistema(client)
        self.consultarPac = ventanaConsultarPaciente()
        self.asignarMedicamento = ventanaMedicamento()
        self.controller1 = ctrl(self.__view, self.system,self.ventanaHC,self.consultarPac,self.asignarMedicamento,self.ventanaPrin)
        self.__view.conexionconelcontrolador(self.controller1) 
        self.ventanaHC.conexionconelcontrolador(self.controller1)
        self.consultarPac.conexionconelcontrolador(self.controller1)
        self.asignarMedicamento.conexionconelcontrolador(self.controller1)
        self.ventanaPrin.conexionconelcontrolador(self.controller1)

    def main(self):
        self.ventanaPrin.show()
        sys.exit(self.__app.exec_())

class ctrl(object):  
    def __init__ (self, view, system, HC,CP,MD,VP):
        self.__view = view
        self.system = system
        self.ventanaHC= HC
        self.consultarPac = CP
        self.asignarMedicamento = MD
        self.ventanaPrin = VP
            
  
    def agregarPacientes(self, cc, nombre, edad):
        self.system.set_cedulaMed(cc)
        self.system.set_nombre(cc, nombre)
        self.system.set_edad(cc, edad)


    # def cambiarPrin_Admin(self):
    #     self.__ventanaPac.show()
    #     self.ventanaPrin.close()
    
    def cambiarPrin_Med(self):
        self.__view.show()
        self.ventanaPrin.close()

    # def cambiarPrin_Pac(self):
    #     self.__ventanaPac.show()
    #     self.ventanaPrin.close()
    
    def buscarensistema(self,cc):

        return self.system.verificar_db(cc)
    
    def buscarensistemaMD(self,cc):

        return self.system.verificar_db(cc)
    
    
    def buscarensistemaCP(self,cc):

        return self.system.verificar_dbCP(cc)

        
    def cambiarMed_HC(self):
        self.ventanaHC.show()
        self.__view.close()

    def cambiarMed_CP(self):
        self.consultarPac.show()
        self.__view.close()

    def cambiarMed_MD(self):
        self.asignarMedicamento.show()
        self.__view.close()

    def cambiarHC_Med(self):
        self.__view.show()
        self.ventanaHC.close()

    def cambiarCP_Med(self):
        self.__view.show()
        self.consultarPac.close()    

    def Guardar_HC(self,cc,HC):
        self.system.set_HC(cc,HC)  

    def asignar_MD(self,cc,MD):
        self.system.set_MD(cc,MD)

    def Guardar_MD(self,cc,MD):
        self.system.set_medicamento(cc,MD)  

    def cambiarMD_Med(self):
        self.__view.show()
        self.asignarMedicamento.close()

    

              
        

if __name__ == "__main__": # el controlador es el encargado de poner en marcha el programa por lo tanto contiene esta linea de codigo
    controller = comunicacion()
    controller.main()