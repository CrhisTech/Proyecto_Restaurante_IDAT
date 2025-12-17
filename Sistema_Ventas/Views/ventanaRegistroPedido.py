# Programando el comportamiento que inicia
#la ventanaRegistroPedidos.py

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

class VentanaRegistroPedidos(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaRegistroPedidos, self).__init__(parent)
        uic.loadUi("UI/Registro_Pedidos.ui", self)
        #self.show()
        
        #Eventos