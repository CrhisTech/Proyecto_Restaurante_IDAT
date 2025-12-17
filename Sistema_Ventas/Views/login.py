#Programando el comportamiento de la ventana
# Login.ui

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLineEdit, QWidget, QApplication, QVBoxLayout
from Views.menuMainAdm import VentanaPrincipalAdm
from Views.menuMainUser import VentanaPrincipalUser

class Login(QtWidgets.QMainWindow):

    contador=0

    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        uic.loadUi("UI/Login.ui", self)
        self.show()

    #Eventos
        self.btnAceptar.clicked.connect(self.iniciarSesion)
        self.btnSalir.clicked.connect(self.cerrar)

    def iniciarSesion(self):
        usuario=self.cboUsuario.currentText().lower()
        passwd=self.txtContra.text().lower()
        if usuario == "administrador" and passwd == "admin":
            self.close()
            vprincipal = VentanaPrincipalAdm(self)
            vprincipal.show()
        elif usuario == "mesero" and passwd == "user":
            self.close()
            vprincipal = VentanaPrincipalUser(self)
            vprincipal.show()
        else:
            self.contador+=1
            QtWidgets.QMessageBox.information(self, "Error: contraseña no válida.",
            "Intento Nro. " + str(self.contador), QtWidgets.QMessageBox.Ok)
            if self.contador == 3:
                QtWidgets.QMessageBox.information(self, "Salida del sistema",
                "Lo sentimos has agotado tus 3 intentos.", QtWidgets.QMessageBox.Ok)
                self.close()

    def cerrar(self):
        self.close()