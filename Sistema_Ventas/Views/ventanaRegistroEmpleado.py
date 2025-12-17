# Programando el comportamiento que inicia
#la ventanaRegistroPedidos.py

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

class VentanaRegistroEmpleado(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaRegistroEmpleado, self).__init__(parent)
        uic.loadUi("UI/Registro_Empleados.ui", self)
        #self.show()
        
        #Eventos