class Reserva():
    def __init__(self, dia =0,mes = 0,anio=0,dni = 0,servicios = [],precio=0,estado = ''):
        self._dia = dia
        self._anio = anio
        self._mes = mes
        self._dni = dni
        self._precio = precio
        self._estado = estado
        self._servicios = servicios
    #Getters
    def get_dia(self):
        return self._dia
    def get_mes(self):
        return self._mes
    def get_anio(self):
        return self._anio
    def get_dni(self):
        return self._dni
    def get_precio(self):
        return self._precio
    def get_estado(self):
        return self._estado
    def get_servicios(self):
        return self._servicios
    #Setters
    def set_dia(self,x):
        self._dia = x
    def set_mes(self,x):
        self._mes = x
    def set_anio(self,x):
        self._anio = x
    def set_dni(self,x):
        self._dni = x
    def set_precio(self,x):
        self._precio = x
    def set_estado(self,x):
        self._estado = x
    def set_servicios(self,x):
        self._servicios = x