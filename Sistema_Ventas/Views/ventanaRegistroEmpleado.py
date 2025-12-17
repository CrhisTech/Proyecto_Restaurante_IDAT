# Programando el comportamiento que inicia
#la ventanaRegistroPedidos.py

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtCore import QDate
import datetime

from Controller.arregloEmpleados import ArregloEmpleados, empleado

aEmp = ArregloEmpleados()

class VentanaRegistroEmpleado(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaRegistroEmpleado, self).__init__(parent)
        uic.loadUi("UI/Registro_Empleados.ui", self)
        #self.show()
        
        #Eventos
        self.Carga_Empleados()
        self.btnGrabar.clicked.connect(self.registrar)
        self.btnBuscar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnLimpiar.clicked.connect(self.quitar)
        self.btnModificar.clicked.connect(self.modificar)
        
    
    def Carga_Empleados(self):
        if aEmp.tamanioArregloEmpleado()==0:
            objEmp= empleado('12345678', 'Alberto', 'Cordero Zamorado', '4585985', 'ATC', '20-12-2024', '22-08-1997')
            aEmp.adicionaEmpleados(objEmp)
            objEmp= empleado('76731957', 'Juan', 'Perez Sanchez', '123456', 'Caja', '20-12-2024', '25-05-1997')
            aEmp.adicionaEmpleados(objEmp)
            objEmp= empleado('12134528', 'Cesar', 'Cespedes Ramos', '4585985', 'Gerencia', '20-12-2024', '12-08-1992')
            aEmp.adicionaEmpleados(objEmp)
            objEmp= empleado('12333378', 'Roberto', 'Chambi Rojas', '4585985', 'Cocina', '20-12-2024', '30-03-1995')
            aEmp.adicionaEmpleados(objEmp)
            self.listar()
        else:
            self.listar()
    
    def obtenerDni(self):
        return self.txtDni.text()
    
    def obtenerNombres(self):
        return self.txtNombres.text()
    
    def obtenerApellidos(self):
        return self.txtApellidos.text()
    
    def obtenerTelefono(self):
        return self.txtTelefono.text()
    
    def obtenerArea(self):
        return self.txtArea.text()
    
    def obtenerFechaIngreso(self):
        return self.dateIngreso.date().toString("dd/MM/yyyy")
    
    def obtenerFechaNacimiento(self):
        return self.dateNacimiento.date().toString("dd/MM/yyyy")
    
    def limpiarTabla(self):
        self.tblEmpleados.clearContents()
        self.tblEmpleados.setRowCount(0)
        
    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del Empleado!"
        elif self.txtNombres.text()=="":
            self.txtNombres.setFocus()
            return "Nombre del Empleado!"
        elif self.txtApellidos.text()=="":
            self.txtApellidos.setFocus()
            return "Apellidos del Empleado!"
        elif self.txtArea.text()=="":
            self.txtArea.setFocus()
            return "Area del Empleado...!!!"
        elif self.txtTelefono.text()=="":
            self.txtTelefono.setFocus()
            return "Telefono del Empleado...!!!"
        elif self.dateIngreso.date().toString("dd/MM/yyyy")=="":
            self.dateIngreso.setFocus()
            return "Fecha de ingreso del Empleado!"
        elif self.dateNacimiento.date().toString("dd/MM/yyyy")=="":
            self.dateNacimiento.setFocus()
            return "Fecha de nacimiento del Empleado!"
        else:
            return ""
        
    def listar(self):
        self.tblEmpleados.setRowCount(aEmp.tamanioArregloEmpleado())
        self.tblEmpleados.setColumnCount(7)
        #Cabecera
        self.tblEmpleados.verticalHeader().setVisible(False)
        for i in range(0, aEmp.tamanioArregloEmpleado()):
            self.tblEmpleados.setItem(i, 0, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getDniEmpleado()))
            self.tblEmpleados.setItem(i, 1, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getNombresEmpleado()))
            self.tblEmpleados.setItem(i, 2, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getApellidosEmpleado()))
            self.tblEmpleados.setItem(i, 4, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getTelefonoEmpleado()))
            self.tblEmpleados.setItem(i, 3, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getAreaEmpleado()))
            fecha_ing = aEmp.devolverEmpleado(i).getFechaIngresoEmpleado()
            if isinstance(fecha_ing, datetime.date):
                fecha_ing = fecha_ing.strftime("%d/%m/%Y")
            fecha_nac = aEmp.devolverEmpleado(i).getFechaNacimientoEmpleado()
            if isinstance(fecha_nac, datetime.date):
                fecha_nac = fecha_nac.strftime("%d/%m/%Y")
            self.tblEmpleados.setItem(i, 5, QtWidgets.QTableWidgetItem(str(fecha_ing)))
            self.tblEmpleados.setItem(i, 6, QtWidgets.QTableWidgetItem(str(fecha_nac)))
            
    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidos.clear()
        self.txtTelefono.clear()
        self.txtArea.clear()
        self.dateIngreso.clear()
        self.dateNacimiento.clear()
        
    # Mantenimientos (Grabar(Registrar), Consultar(Buscar), Modificar, Listar, Quitar(Eliminar))
    def registrar(self):
        if self.valida() == "":
            objEmp=empleado(self.obtenerDni(), self.obtenerNombres(), self.obtenerApellidos(), self.obtenerTelefono(),
                            self.obtenerArea(), self.obtenerFechaIngreso(), self.obtenerFechaNacimiento())
            dni = self.obtenerDni()
            if aEmp.buscarEmpleado(dni) == -1:
                aEmp.adicionaEmpleados(objEmp)
                #aEmp.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Empleado", "El DNI ingreado ya existe!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado", 
                                              "Error en" + self.valida(), QtWidgets.QMessageBox.Ok)
            
    def consultar(self):
        #self.LimpiarTabla()
        if aEmp.tamanioArregloEmpleado()==0:
            QtWidgets.QMessageBox.information(self, "Consultar Empleado", "No existe empleado a consultar!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            dni= self.txtBuscar.text()
            pos = aEmp.buscarEmpleado(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Empente",
                                                  "El DNI ingresado no existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
            else:
                fecha_ing = aEmp.devolverEmpleado(pos).getFechaIngresoEmpleado()
                if isinstance(fecha_ing, datetime.date):
                    fecha_ing = fecha_ing.strftime("%d/%m/%Y")
                fecha_nac = aEmp.devolverEmpleado(pos).getFechaNacimientoEmpleado()
                if isinstance(fecha_nac, datetime.date):
                    fecha_nac = fecha_nac.strftime("%d/%m/%Y")
                self.txtDni.setText(aEmp.devolverEmpleado(pos).getDniEmpleado())
                self.txtNombres.setText(aEmp.devolverEmpleado(pos).getNombresEmpleado())
                self.txtApellidos.setText(aEmp.devolverEmpleado(pos).getApellidosEmpleado())
                self.txtTelefono.setText(aEmp.devolverEmpleado(pos).getTelefonoEmpleado())
                self.txtArea.setText(aEmp.devolverEmpleado(pos).getAreaEmpleado())
                self.dateIngreso.setDate(aEmp.devolverEmpleado(pos).getFechaIngresoEmpleado())
                self.dateNacimiento.setDate(aEmp.devolverEmpleado(pos).getFechaNacimientoEmpleado())
                
                self.tblEmpleados.setRowCount(1)
                self.tblEmpleados.setItem(0, 0, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getDniEmpleado()))
                self.tblEmpleados.setItem(0, 1, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getNombresEmpleado()))
                self.tblEmpleados.setItem(0, 2, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getApellidosEmpleado()))
                self.tblEmpleados.setItem(0, 4, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getTelefonoEmpleado()))
                self.tblEmpleados.setItem(0, 3, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getAreaEmpleado()))
                self.tblEmpleados.setItem(0, 5, QtWidgets.QTableWidgetItem(str(fecha_ing)))
                self.tblEmpleados.setItem(0, 6, QtWidgets.QTableWidgetItem(str(fecha_nac)))
                
    def eliminar(self):
        if self.obtenerDni()=="":
            QtWidgets.QMessageBox.information(self, "Consultar Empleado",
            "Por favor Consultar el dni...",
            QtWidgets.QMessageBox.Ok)
        else:
            dni = self.txtDni.text()
            pos = aEmp.buscarEmpleado(dni)
            aEmp.eliminarEmpleado(pos)
            #aEmp.grabar()
            self.limpiarControles()
            self.listar()

    def quitar(self):
        if aEmp.tamanioArregloEmpleado() ==0:
            QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                              "No existe Empleado a eliminar... !!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            fila=self.tblEmpleados.selectedItems()
            if fila:
                indiceFila=fila[0].row()
                dni=self.tblEmpleados.item(indiceFila, 0).text()
                pos =aEmp.buscarEmpleado(dni)
                aEmp.eliminarEmpleado(pos)
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                                  "Debe seleccionar una fila... !!!",
                                                  QtWidgets.QMessageBox.Ok)
                


    def modificar(self):
        if self.obtenerDni()=="":
            QtWidgets.QMessageBox.information(self, "Consultar Empente",
            "Por favor Consultar el dni...",
            QtWidgets.QMessageBox.Ok)
        
        if aEmp.tamanioArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Empente",
                                                  "No existen Empentes a Modificar... !!!",
						   QtWidgets.QMessageBox.Ok)
        else:
            dni= self.obtenerDni()
            pos= aEmp.buscarEmpleado(dni)
            if pos != -1:
                objEmp= empleado(self.obtenerDni(), self.obtenerNombres(),
                                 self.obtenerApellidos(),
                                 self.obtenerTelefono(),
                                 self.obtenerArea(),self.obtenerFechaIngreso(),
                                 self.obtenerFechaNacimiento())
                aEmp.modificarEmpleado(objEmp, pos)
                #aEmp.grabar()
                self.limpiarControles()
                self.listar()
        