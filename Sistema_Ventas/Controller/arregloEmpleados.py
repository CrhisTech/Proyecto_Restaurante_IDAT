from Controller.empleados import empleado

#MANTENIMIENTO

class ArregloEmpleados():
    # Atributos de clase
    dataEmpleados = [] #Mostrar base de datos
    
    #Constructores
    def __init__(self):
        pass
    
    def adicionaEmpleados(self, objemp):
        self.dataEmpleados.append(objemp)
    
    def devolverEmpleado(self, pos):
        return self.dataEmpleados[pos]
    
    def tamanioArregloEmpleado(self):
        return len(self.dataEmpleados)
    
    def buscarEmpleado(self, dni):
        for i in range(self.tamanioArregloEmpleado()):
            if dni == self.dataEmpleados[i].getDniEmpleado():
                return i #DEVOLVER POSICION DEL ELEMENTO
        return -1
    
    def eliminarEmpleado(self, pos): #ELIMINAR EMPLEADO
        del(self.dataEmpleados[pos])
        
    def modificarEmpleado(self, objemp, pos): #MODIFICAR DATO
        self.dataEmpleados[pos] = objemp
        
    def retornarDatos(self): #RETORNAR DATOS
        return self.dataEmpleados