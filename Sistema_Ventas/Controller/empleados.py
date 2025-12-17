class empleado():
    #1 atributos de clase (Encapsulados)
    __dniEmpleado = ""; __nombresEmpleado="";
    __apellidosEmpleado=""; __telefonoEmpleado="";
    __areaEmpleado=""; __fechaIngresoEmpleado="";
    __fechaNacimientoEmpleado="";
    
    #2 constructor
    def __init__(self, dniEmpleado, nombresEmpleado, apellidosEmpleado, telefonoEmpleado, areaEmpleado, fechaIngresoEmpleado, fechaNacimientoEmpleado):
        self.__dniEmpleado = dniEmpleado
        self.__nombresEmpleado = nombresEmpleado
        self.__apellidosEmpleado = apellidosEmpleado
        self.__telefonoEmpleado = telefonoEmpleado
        self.__areaEmpleado = areaEmpleado
        self.__fechaIngresoEmpleado = fechaIngresoEmpleado
        self.__fechaNacimientoEmpleado = fechaNacimientoEmpleado
        
    def getDniEmpleado(self):
        return self.__dniEmpleado
    def setDniEmpleado(self, dniEmpleado):
        self.__dniEmpleado = dniEmpleado
        
    def getNombresEmpleado(self):
        return self.__nombresEmpleado
    def setNombresEmpleado(self, nombresEmpleado):
        self.__nombresEmpleado = nombresEmpleado
        
    def getApellidosEmpleado(self):
        return self.__apellidosEmpleado
    def setApellidosEmpleado(self, apellidosEmpleado):
        self.__apellidosEmpleado = apellidosEmpleado
        
    def getTelefonoEmpleado(self):
        return self.__telefonoEmpleado
    def setTelefonoEmpleado(self, telefonoEmpleado):
        self.__telefonoEmpleado = telefonoEmpleado
    
    def getAreaEmpleado(self):
        return self.__areaEmpleado
    def setAreaEmpleado(self, areaEmpleado):
        self.__dniEmpleado = areaEmpleado
    
    def getFechaIngresoEmpleado(self):
        return self.__fechaIngresoEmpleado
    def setFechaIngresoEmpleado(self, fechaIngresoEmpleado):
        self.__fechaIngresoEmpleado = fechaIngresoEmpleado
    
    def getFechaNacimientoEmpleado(self):
        return self.__fechaNacimientoEmpleado
    def setFechaNacimientoEmpleado(self, fechaNacimientoEmpleado):
        self.__fechaNacimientoEmpleado = fechaNacimientoEmpleado