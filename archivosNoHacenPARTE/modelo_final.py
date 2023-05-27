import pymongo
import scipy.io as sio
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import cv2


url ="mongodb+srv://samuelra2003:samuel@cluster0.pmzsboi.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
db = client.test

class Sistema(): 
    def __init__ (self, client):
        mydb = client["Hospital"]
        self.__medicos = mydb["Médicos"]
        self.__pacientes = mydb["Pacientes"]
        self.__admin = mydb["Admin"]
    #### MEDICOS
    def set_cedulaMed(self, cedula):
        self.__medicos.insert_one({'Cedula':cedula})

    def set_nombre(self, cedula, nombre):
        myquery = {'Cedula':cedula}
        newvalues = {"$set": {"Nombre":nombre}}
        self.__medicos.update_one(myquery, newvalues)

    def set_edad(self, cedula, edad):
        myquery = {'Cedula':cedula}
        newvalues = {"$set": {"Edad":edad}}
        self.__medicos.update_one(myquery, newvalues)

    def set_HC(self,cedula,HC):
        myquery = {'Cedula':cedula}
        newvalues = {"$set": {"Historia clinica":HC}}
        self.__medicos.update_one(myquery, newvalues)

    def set_medicamento(self,cedula,MD):
        myquery = {'Cedula':cedula}
        newvalues = {"$set": {"Medicamentos":MD}}
        self.__medicos.update_one(myquery, newvalues)
    
    

    ### PACIENTES
    def set_cedulaPac(self, cedula):
        self.__pacientes.insert_one({'Cedula':cedula})
    

    def set_nombrePac(self, cedula, nombre):
        myquery = {'Cedula':cedula}
        newvalues = {"$set": {"Nombre":nombre}}
        self.__pacientes.update_one(myquery, newvalues)

    def set_edadPac(self, cedula, edad):
        myquery = {'Cedula':cedula}
        newvalues = {"$set": {"Edad":edad}}
        self.__pacientes.update_one(myquery, newvalues)

    def verificar_db(self,cedula):
        ver = list(self.__medicos.find( { "Cedula": cedula }))
        print(ver)
        if ver == None:
            print("hola2")
            return None
            
        else:
            return True
        
    def verificar_dbCP(self,cedula):
        ver = list(self.__medicos.find( { "Cedula": cedula }))
        print(ver)
        if ver == None:
            print("hola2")
            return None
            
        else:
            return ver
     ### ADMIN
    def set_cedulaAdm(self, cedula):
        self.__admin.insert_one({'Cedula':cedula})

    def set_nombreAdm(self, cedula, nombre):
        myquery = {'Cedula':cedula}
        newvalues = {"$set": {"Nombre":nombre}}
        self.__admin.update_one(myquery, newvalues)

    def set_edadAdm(self, cedula, edad):
        myquery = {'Cedula':cedula}
        newvalues = {"$set": {"Edad":edad}}
        self.__admin.update_one(myquery, newvalues)   