# Programando el comportamiento que inicia
#la ventanaRegistroPedidos.py

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

class VentanaRegistroProducto(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaRegistroProducto, self).__init__(parent)
        uic.loadUi("UI/Registro_Productos.ui", self)
        #self.show()
        
        #Eventos