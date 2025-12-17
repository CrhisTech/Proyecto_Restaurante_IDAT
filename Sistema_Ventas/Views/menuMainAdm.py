#Programando la ventanaPrincipal.py
# y su comportamiento inicial

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

from Views.ventanaRegistroEmpleado import VentanaRegistroEmpleado
from Views.ventanaRegistroProducto import VentanaRegistroProducto
from Views.ventanaRegistroPedido import VentanaRegistroPedidos

class VentanaPrincipalAdm(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaPrincipalAdm, self).__init__(parent)
        uic.loadUi("UI/menuMainAdm.ui", self)
        #self.show()
    #Eventos
        self.btnEmpleado.clicked.connect(self.abriVentanaRegistroEmpleado)
        self.btnProducto.clicked.connect(self.abrirVentanaRegistroProducto)
        self.btnPedidos.clicked.connect(self.abrirVentanaRegistroPedidos)
        self.btnCerrar.clicked.connect(self.cerrar)

    def abriVentanaRegistroEmpleado(self):
        vregistroEmpleado= VentanaRegistroEmpleado(self)
        vregistroEmpleado.show()

    def abrirVentanaRegistroProducto(self):
        vregistroProducto = VentanaRegistroProducto(self)
        vregistroProducto.show()

    def abrirVentanaRegistroPedidos(self):
        vregistroPedido = VentanaRegistroPedidos(self)
        vregistroPedido.show()

    def cerrar(self):
        self.close()