class Persona:
    def __init__(self,nombre = "",apellido= "",dni=0):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
    #Getters
    def get_nombre(self):
        return self._nombre
    def get_apellido(self):
        return self._apellido
    def get_dni(self):
        return self._dni
    #Setters
    def set_nombre(self,x):
        self._nombre = x
    def set_apellido(self,x):
        self._apellido = x
    def set_dni(self,x):
        self._dni = x
        
    def get_info(self):
        return(f'nombre: {self.get_nombre()}, apellido: {self.get_apellido()}, dni: {self.get_dni()}')
    def __str__(self):
        return(f'{self.get_nombre()},{self.get_apellido()},{self.get_dni()}')
