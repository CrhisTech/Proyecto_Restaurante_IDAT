#Programando el menuMainUser.py
# y su comportamiento inicial

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

from Views.ventanaRegistroPedido import VentanaRegistroPedidos

class VentanaPrincipalUser(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipalUser, self).__init__(parent)
        uic.loadUi("UI/menuMainUser.ui", self)
        #self.show()

#Eventos
        self.btnPedidos.clicked.connect(self.abrirVentanaRegistroPedidos)
        self.btnCerrar.clicked.connect(self.cerrar)

    def abrirVentanaRegistroPedidos(self):
        vregistroPedidos= VentanaRegistroPedidos(self)
        vregistroPedidos.show()

    def cerrar(self):
        self.close()